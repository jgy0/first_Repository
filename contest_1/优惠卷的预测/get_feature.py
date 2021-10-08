# coding:utf-8

import re
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import roc_auc_score

offline_train = pd.read_csv(r'D:\编程资料\第六课综合实战：电商智能推荐-优惠券使用预测\数据、代码及PPT\2.数据\ccf_offline_stage1_train.csv',
                           parse_dates=['Date_received', 'Date'])
# 正例索引
index_ture = (offline_train['Date']-offline_train['Date_received']).apply(lambda x: x.days <= 15)
# 反例索引
index_false_1 = (offline_train['Date']-offline_train['Date_received']).apply(lambda x: x.days > 15)
index_false_2 = offline_train['Date_received'].notnull() & offline_train['Date'].isnull()

# 打上标签
offline_train['label'] = -1  # 普通用户
offline_train.loc[index_ture, 'label'] = 1  # 正样本
offline_train.loc[(index_false_1 | index_false_2), 'label'] = 0  # 反样本
offline_train['label'].value_counts()



def getdiscount(string=None):
    try:
        if re.findall('\d+:\d+', string) !=[]:
            return 1-float(string.split(':')[1])/float(string.split(':')[0])
        else:
            return float(string)
    except:
        return  1.0


offline_train['Discount_rate'] = offline_train['Discount_rate'].apply(getdiscount) # 特征一优惠劵的折扣
offline_train['Discount_rate'].unique()
offline_train['Distance'].unique()
offline_train['Distance'].fillna(method='ffill', inplace=True)   # method='ffill' 用空值的前一个数填充空值(特征二)
# string = '200:20'
# string = '0.9'
# string =np.nan
Coupon_popu = offline_train[['Coupon_id', 'label']].groupby('Coupon_id').agg(lambda x: sum(x == 1)/sum(x != -1)) #特征三优惠卷的流行度
number_user_merchant = offline_train[['User_id', 'Merchant_id', 'Date']].groupby(['User_id', 'Merchant_id']).agg(lambda x: sum(x.notnull()))  # 特征四优惠劵的使用次数

# 重命名列名称

Coupon_popu.columns = ['Coupon_popu']
number_user_merchant.columns = ['number_user_merchant']

offline_train_3 = pd.merge(offline_train, Coupon_popu, left_on='Coupon_id', right_index=True, how='left')   # 特征三的拼接
offline_train_4 = pd.merge(offline_train_3, number_user_merchant, left_on=['User_id', 'Merchant_id'], right_index=True, how='left')    # 特征四的拼接



def train(model=GradientBoostingClassifier(n_estimators=100,max_depth=3), data=None, feature=['Discount_rate','Distance']
          , label='label', number_pos=64395, number_ne=988887):
    offline_train=data
    # number_pos = 64395  # 正样本数量
    # number_ne = 988887  # 负样本数量
    a = offline_train[offline_train['label']==1].sample(number_pos)
    b = offline_train[offline_train['label']==0].sample(number_ne)
    c = a.append(b)
    X = c.loc[:, feature]
    y = c[label]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)  # 通常在这种类分布不平衡的情况下会用到stratify。

    model.fit(X_train, y_train)
    pre =model.predict_proba(X_test)[:, 1]
    # pre.shape
    # (210657,)
    auc = roc_auc_score(y_test, pre)
    return model, auc


model, auc = train(data=offline_train)

offline_test=pd.read_csv(r'D:\编程资料\第六课综合实战：电商智能推荐-优惠券使用预测\数据、代码及PPT\2.数据\ccf_offline_stage1_test_revised.csv')
offline_test['Discount_rate'] = offline_test['Discount_rate'].apply(getdiscount)   # 特征一
offline_test['Distance'].fillna(method='ffill', inplace=True)      # 特征二
offline_test3 = pd.merge(offline_test, Coupon_popu, left_on='Coupon_id', right_index=True, how='left')
offline_test4 = pd.merge(offline_test3, number_user_merchant, left_on=['User_id', 'Merchant_id'], right_index=True, how='left')
feature_pre = ['Discount_rate', 'Distance']


def predict(model=None, data=offline_test, features_predict=None, out_file=None):
    X_pre=data.loc[:, features_predict]
    probe=model.predict_proba(X_pre)[:, 1]
    result = data[['User_id', 'Coupon_id', 'Date_received']]
    result['Pro']=probe
    result.to_csv(out_file, index=None, header=None)
    return result


predict(model=model, data=offline_test, features_predict=['Discount_rate', 'Distance'], out_file=r'D:\编程资料\result.csv')




