import numpy as np
import pandas as pd
import subprocess
###################################################################################
### L5
###################################################################################
#df_L5=df_L5.drop(['Unnamed: 0'],axis=1)
df_L5 = pd.read_csv('files/network_L5.csv')
df_L5['packet']=1
Time_L5 = df_L5['Time']
MI_dir_L5_weight = df_L5.groupby('MI')['packet'].transform(lambda x: x/x.sum())
MI_dir_L5_mean = df_L5.groupby('MI')['pkt_size'].transform(lambda x: np.mean(x))
MI_dir_L5_variance = df_L5.groupby('MI')['pkt_size'].transform(lambda x: np.var(x))
H_L5_weight = df_L5.groupby('H')['packet'].transform(lambda x: x/x.sum())
H_L5_mean = df_L5.groupby('H')['pkt_size'].transform(lambda x: np.mean(x))
H_L5_variance = df_L5.groupby('H')['pkt_size'].transform(lambda x: np.var(x))
HH_L5_weight = df_L5.groupby('HH')['packet'].transform(lambda x: x/x.sum())
HH_L5_mean = df_L5.groupby('HH')['pkt_size'].transform(lambda x: np.mean(x))
HH_L5_std = df_L5.groupby('HH')['pkt_size'].transform(lambda x: np.std(x))
HH_L5_magnitude = df_L5.groupby('HH')['pkt_size'].transform(lambda x: np.linalg.norm(x))
HH_L5_radius = df_L5.groupby('HH')['pkt_size'].transform(lambda x: np.radians(x))
HH_L5_covariance = df_L5.groupby('HH')['pkt_size'].transform(lambda x: np.cov(x))
HH_L5_pcc = df_L5.groupby('HH')['pkt_size'].transform(lambda x: np.corrcoef(x))
HH_jit_L5_weight = df_L5.groupby('HH')['HH_jit'].transform(lambda x: x/x.sum())
HH_jit_L5_mean = df_L5.groupby('HH')['HH_jit'].transform(lambda x: np.mean(x))
HH_jit_L5_variance = df_L5.groupby('HH')['HH_jit'].transform(lambda x: np.var(x))
HpHp_L5_weight = df_L5.groupby('HpHp')['packet'].transform(lambda x: x/x.sum())
HpHp_L5_mean = df_L5.groupby('HpHp')['pkt_size'].transform(lambda x: np.mean(x))
HpHp_L5_std = df_L5.groupby('HpHp')['pkt_size'].transform(lambda x: np.std(x))
HpHp_L5_magnitude = df_L5.groupby('HpHp')['pkt_size'].transform(lambda x: np.linalg.norm(x))
HpHp_L5_radius = df_L5.groupby('HpHp')['pkt_size'].transform(lambda x: np.radians(x))
HpHp_L5_covariance = df_L5.groupby('HpHp')['pkt_size'].transform(lambda x: np.cov(x))
HpHp_L5_pcc = df_L5.groupby('HpHp')['pkt_size'].transform(lambda x: np.corrcoef(x))
###################################################################################
### L3
###################################################################################
#df_L3 = pd.read_csv('network_L3.csv')
#df_L3=df_L3.drop(['Unnamed: 0'],axis=1)
df_L3 = pd.read_csv('files/network_L3.csv')
df_L3['packet']=1
Time_L3 = df_L3['Time']
MI_dir_L3_weight = df_L3.groupby('MI')['packet'].transform(lambda x: x/x.sum())
MI_dir_L3_mean = df_L3.groupby('MI')['pkt_size'].transform(lambda x: np.mean(x))
MI_dir_L3_variance = df_L3.groupby('MI')['pkt_size'].transform(lambda x: np.var(x))
H_L3_weight = df_L3.groupby('H')['packet'].transform(lambda x: x/x.sum())
H_L3_mean = df_L3.groupby('H')['pkt_size'].transform(lambda x: np.mean(x))
H_L3_variance = df_L3.groupby('H')['pkt_size'].transform(lambda x: np.var(x))
HH_L3_weight = df_L3.groupby('HH')['packet'].transform(lambda x: x/x.sum())
HH_L3_mean = df_L3.groupby('HH')['pkt_size'].transform(lambda x: np.mean(x))
HH_L3_std = df_L3.groupby('HH')['pkt_size'].transform(lambda x: np.std(x))
HH_L3_magnitude = df_L3.groupby('HH')['pkt_size'].transform(lambda x: np.linalg.norm(x))
HH_L3_radius = df_L3.groupby('HH')['pkt_size'].transform(lambda x: np.radians(x))
HH_L3_covariance = df_L3.groupby('HH')['pkt_size'].transform(lambda x: np.cov(x))
HH_L3_pcc = df_L3.groupby('HH')['pkt_size'].transform(lambda x: np.corrcoef(x))
HH_jit_L3_weight = df_L3.groupby('HH')['HH_jit'].transform(lambda x: x/x.sum())
HH_jit_L3_mean = df_L3.groupby('HH')['HH_jit'].transform(lambda x: np.mean(x))
HH_jit_L3_variance = df_L3.groupby('HH')['HH_jit'].transform(lambda x: np.var(x))
HpHp_L3_weight = df_L3.groupby('HpHp')['packet'].transform(lambda x: x/x.sum())
HpHp_L3_mean = df_L3.groupby('HpHp')['pkt_size'].transform(lambda x: np.mean(x))
HpHp_L3_std = df_L3.groupby('HpHp')['pkt_size'].transform(lambda x: np.std(x))
HpHp_L3_magnitude = df_L3.groupby('HpHp')['pkt_size'].transform(lambda x: np.linalg.norm(x))
HpHp_L3_radius = df_L3.groupby('HpHp')['pkt_size'].transform(lambda x: np.radians(x))
HpHp_L3_covariance = df_L3.groupby('HpHp')['pkt_size'].transform(lambda x: np.cov(x))
HpHp_L3_pcc = df_L3.groupby('HpHp')['pkt_size'].transform(lambda x: np.corrcoef(x))

###################################################################################
### L1
###################################################################################
df_L1 = pd.read_csv('files/network_L1.csv')
#df_L1=df_L1.drop(['Unnamed: 0'],axis=1)
df_L1['packet']=1
Time_L1 = df_L1['Time']
MI_dir_L1_weight = df_L1.groupby('MI')['packet'].transform(lambda x: x/x.sum())
MI_dir_L1_mean = df_L1.groupby('MI')['pkt_size'].transform(lambda x: np.mean(x))
MI_dir_L1_variance = df_L1.groupby('MI')['pkt_size'].transform(lambda x: np.var(x))
H_L1_weight = df_L1.groupby('H')['packet'].transform(lambda x: x/x.sum())
H_L1_mean = df_L1.groupby('H')['pkt_size'].transform(lambda x: np.mean(x))
H_L1_variance = df_L1.groupby('H')['pkt_size'].transform(lambda x: np.var(x))
HH_L1_weight = df_L1.groupby('HH')['packet'].transform(lambda x: x/x.sum())
HH_L1_mean = df_L1.groupby('HH')['pkt_size'].transform(lambda x: np.mean(x))
HH_L1_std = df_L1.groupby('HH')['pkt_size'].transform(lambda x: np.std(x))
HH_L1_magnitude = df_L1.groupby('HH')['pkt_size'].transform(lambda x: np.linalg.norm(x))
HH_L1_radius = df_L1.groupby('HH')['pkt_size'].transform(lambda x: np.radians(x))
HH_L1_covariance = df_L1.groupby('HH')['pkt_size'].transform(lambda x: np.cov(x))
HH_L1_pcc = df_L1.groupby('HH')['pkt_size'].transform(lambda x: np.corrcoef(x))
HH_jit_L1_weight = df_L1.groupby('HH')['HH_jit'].transform(lambda x: x/x.sum())
HH_jit_L1_mean = df_L1.groupby('HH')['HH_jit'].transform(lambda x: np.mean(x))
HH_jit_L1_variance = df_L1.groupby('HH')['HH_jit'].transform(lambda x: np.var(x))
HpHp_L1_weight = df_L1.groupby('HpHp')['packet'].transform(lambda x: x/x.sum())
HpHp_L1_mean = df_L1.groupby('HpHp')['pkt_size'].transform(lambda x: np.mean(x))
HpHp_L1_std = df_L1.groupby('HpHp')['pkt_size'].transform(lambda x: np.std(x))
HpHp_L1_magnitude = df_L1.groupby('HpHp')['pkt_size'].transform(lambda x: np.linalg.norm(x))
HpHp_L1_radius = df_L1.groupby('HpHp')['pkt_size'].transform(lambda x: np.radians(x))
HpHp_L1_covariance = df_L1.groupby('HpHp')['pkt_size'].transform(lambda x: np.cov(x))
HpHp_L1_pcc = df_L1.groupby('HpHp')['pkt_size'].transform(lambda x: np.corrcoef(x))

###################################################################################
### L0.1
###################################################################################
df_L0_1 = pd.read_csv('files/network_L0.1.csv')
#df_L0_1=df_L0_1.drop(['Unnamed: 0'],axis=1)
df_L0_1['packet']=1
Time_L0_1 = df_L0_1['Time']
MI_dir_L0_1_weight = df_L0_1.groupby('MI')['packet'].transform(lambda x: x/x.sum())
MI_dir_L0_1_mean = df_L0_1.groupby('MI')['pkt_size'].transform(lambda x: np.mean(x))
MI_dir_L0_1_variance = df_L0_1.groupby('MI')['pkt_size'].transform(lambda x: np.var(x))
H_L0_1_weight = df_L0_1.groupby('H')['packet'].transform(lambda x: x/x.sum())
H_L0_1_mean = df_L0_1.groupby('H')['pkt_size'].transform(lambda x: np.mean(x))
H_L0_1_variance = df_L0_1.groupby('H')['pkt_size'].transform(lambda x: np.var(x))
HH_L0_1_weight = df_L0_1.groupby('HH')['packet'].transform(lambda x: x/x.sum())
HH_L0_1_mean = df_L0_1.groupby('HH')['pkt_size'].transform(lambda x: np.mean(x))
HH_L0_1_std = df_L0_1.groupby('HH')['pkt_size'].transform(lambda x: np.std(x))
HH_L0_1_magnitude = df_L0_1.groupby('HH')['pkt_size'].transform(lambda x: np.linalg.norm(x))
HH_L0_1_radius = df_L0_1.groupby('HH')['pkt_size'].transform(lambda x: np.radians(x))
HH_L0_1_covariance = df_L0_1.groupby('HH')['pkt_size'].transform(lambda x: np.cov(x))
HH_L0_1_pcc = df_L0_1.groupby('HH')['pkt_size'].transform(lambda x: np.corrcoef(x))
HH_jit_L0_1_weight = df_L0_1.groupby('HH')['HH_jit'].transform(lambda x: x/x.sum())
HH_jit_L0_1_mean = df_L0_1.groupby('HH')['HH_jit'].transform(lambda x: np.mean(x))
HH_jit_L0_1_variance = df_L0_1.groupby('HH')['HH_jit'].transform(lambda x: np.var(x))
HpHp_L0_1_weight = df_L0_1.groupby('HpHp')['packet'].transform(lambda x: x/x.sum())
HpHp_L0_1_mean = df_L0_1.groupby('HpHp')['pkt_size'].transform(lambda x: np.mean(x))
HpHp_L0_1_std = df_L0_1.groupby('HpHp')['pkt_size'].transform(lambda x: np.std(x))
HpHp_L0_1_magnitude = df_L0_1.groupby('HpHp')['pkt_size'].transform(lambda x: np.linalg.norm(x))
HpHp_L0_1_radius = df_L0_1.groupby('HpHp')['pkt_size'].transform(lambda x: np.radians(x))
HpHp_L0_1_covariance = df_L0_1.groupby('HpHp')['pkt_size'].transform(lambda x: np.cov(x))
HpHp_L0_1_pcc = df_L0_1.groupby('HpHp')['pkt_size'].transform(lambda x: np.corrcoef(x))

###################################################################################
### L0.01
###################################################################################
df_L0_01 = pd.read_csv('files/network_L0.01.csv')
#df_L0_01=df_L0_01.drop(['Unnamed: 0'],axis=1)
df_L0_01['packet']=1
Time_L0_01 = df_L0_01['Time']
MI_dir_L0_01_weight = df_L0_01.groupby('MI')['packet'].transform(lambda x: x/x.sum())
MI_dir_L0_01_mean = df_L0_01.groupby('MI')['pkt_size'].transform(lambda x: np.mean(x))
MI_dir_L0_01_variance = df_L0_01.groupby('MI')['pkt_size'].transform(lambda x: np.var(x))
H_L0_01_weight = df_L0_01.groupby('H')['packet'].transform(lambda x: x/x.sum())
H_L0_01_mean = df_L0_01.groupby('H')['pkt_size'].transform(lambda x: np.mean(x))
H_L0_01_variance = df_L0_01.groupby('H')['pkt_size'].transform(lambda x: np.var(x))
HH_L0_01_weight = df_L0_01.groupby('HH')['packet'].transform(lambda x: x/x.sum())
HH_L0_01_mean = df_L0_01.groupby('HH')['pkt_size'].transform(lambda x: np.mean(x))
HH_L0_01_std = df_L0_01.groupby('HH')['pkt_size'].transform(lambda x: np.std(x))
HH_L0_01_magnitude = df_L0_01.groupby('HH')['pkt_size'].transform(lambda x: np.linalg.norm(x))
HH_L0_01_radius = df_L0_01.groupby('HH')['pkt_size'].transform(lambda x: np.radians(x))
HH_L0_01_covariance = df_L0_01.groupby('HH')['pkt_size'].transform(lambda x: np.cov(x))
HH_L0_01_pcc = df_L0_01.groupby('HH')['pkt_size'].transform(lambda x: np.corrcoef(x))
HH_jit_L0_01_weight = df_L0_01.groupby('HH')['HH_jit'].transform(lambda x: x/x.sum())
HH_jit_L0_01_mean = df_L0_01.groupby('HH')['HH_jit'].transform(lambda x: np.mean(x))
HH_jit_L0_01_variance = df_L0_01.groupby('HH')['HH_jit'].transform(lambda x: np.var(x))
HpHp_L0_01_weight = df_L0_01.groupby('HpHp')['packet'].transform(lambda x: x/x.sum())
HpHp_L0_01_mean = df_L0_01.groupby('HpHp')['pkt_size'].transform(lambda x: np.mean(x))
HpHp_L0_01_std = df_L0_01.groupby('HpHp')['pkt_size'].transform(lambda x: np.std(x))
HpHp_L0_01_magnitude = df_L0_01.groupby('HpHp')['pkt_size'].transform(lambda x: np.linalg.norm(x))
HpHp_L0_01_radius = df_L0_01.groupby('HpHp')['pkt_size'].transform(lambda x: np.radians(x))
HpHp_L0_01_covariance = df_L0_01.groupby('HpHp')['pkt_size'].transform(lambda x: np.cov(x))
HpHp_L0_01_pcc = df_L0_01.groupby('HpHp')['pkt_size'].transform(lambda x: np.corrcoef(x))

###################################################################################
### creating dataframe
###################################################################################

df = pd.DataFrame({"MI_dir_L5_weight":MI_dir_L5_weight})
df["MI_dir_L5_mean"]=MI_dir_L5_mean
df["MI_dir_L5_variance"]=MI_dir_L5_variance
df["MI_dir_L3_weight"]=MI_dir_L3_weight
df["MI_dir_L3_mean"]=MI_dir_L3_mean
df["MI_dir_L3_variance"]=MI_dir_L3_variance
df["MI_dir_L1_weight"]=MI_dir_L1_weight
df["MI_dir_L1_mean"]=MI_dir_L1_mean
df["MI_dir_L1_variance"]=MI_dir_L1_variance
df["MI_dir_L0.1_weight"]=MI_dir_L0_1_weight
df["MI_dir_L0.1_mean"]=MI_dir_L0_1_mean
df["MI_dir_L0.1_variance"]=MI_dir_L0_1_variance
df["MI_dir_L0.01_weight"]=MI_dir_L0_01_weight
df["MI_dir_L0.01_mean"]=MI_dir_L0_01_mean
df["MI_dir_L0.01_variance"]=MI_dir_L0_01_variance
df["H_L5_weight"]=H_L5_weight
df["H_L5_mean"]=H_L5_mean
df["H_L5_variance"]=H_L5_variance
df["H_L3_weight"]=H_L3_weight
df["H_L3_mean"]=H_L3_mean
df["H_L3_variance"]=H_L3_variance
df["H_L1_weight"]=H_L1_weight
df["H_L1_mean"]=H_L1_mean
df["H_L1_variance"]=H_L1_variance
df["H_L0.1_weight"]=H_L0_1_weight
df["H_L0.1_mean"]=H_L0_1_mean
df["H_L0.1_variance"]=H_L0_1_variance
df["H_L0.01_weight"]=H_L0_01_weight
df["H_L0.01_mean"]=H_L0_01_mean
df["H_L0.01_variance"]=H_L0_01_variance
df["HH_L5_weight"]=HH_L5_weight
df["HH_L5_mean"]=HH_L5_mean
df["HH_L5_std"]=HH_L5_std
df["HH_L5_magnitude"]=HH_L5_magnitude
df["HH_L5_radius"]=HH_L5_radius
df["HH_L5_covariance"]=HH_L5_covariance
df["HH_L5_pcc"]=HH_L5_pcc
df["HH_L3_weight"]=HH_L3_weight
df["HH_L3_mean"]=HH_L3_mean
df["HH_L3_std"]=HH_L3_std
df["HH_L3_magnitude"]=HH_L3_magnitude
df["HH_L3_radius"]=HH_L3_radius
df["HH_L3_covariance"]=HH_L3_covariance
df["HH_L3_pcc"]=HH_L3_pcc
df["HH_L1_weight"]=HH_L1_weight
df["HH_L1_mean"]=HH_L1_mean
df["HH_L1_std"]=HH_L1_std
df["HH_L1_magnitude"]=HH_L1_magnitude
df["HH_L1_radius"]=HH_L1_radius
df["HH_L1_covariance"]=HH_L1_covariance
df["HH_L1_pcc"]=HH_L1_pcc
df["HH_L0.1_weight"]=HH_L0_1_weight
df["HH_L0.1_mean"]=HH_L0_1_mean
df["HH_L0.1_std"]=HH_L0_1_std
df["HH_L0.1_magnitude"]=HH_L0_1_magnitude
df["HH_L0.1_radius"]=HH_L0_1_radius
df["HH_L0.1_covariance"]=HH_L0_1_covariance
df["HH_L0.1_pcc"]=HH_L0_1_pcc
df["HH_L0.01_weight"]=HH_L0_01_weight
df["HH_L0.01_mean"]=HH_L0_01_mean
df["HH_L0.01_std"]=HH_L0_01_std
df["HH_L0.01_magnitude"]=HH_L0_01_magnitude
df["HH_L0.01_radius"]=HH_L0_01_radius
df["HH_L0.01_covariance"]=HH_L0_01_covariance
df["HH_L0.01_pcc"]=HH_L0_01_pcc
df["HH_jit_L5_weight"]=HH_jit_L5_weight
df["HH_jit_L5_mean"]=HH_jit_L5_mean
df["HH_jit_L5_variance"]=HH_jit_L5_variance
df["HH_jit_L3_weight"]=HH_jit_L3_weight
df["HH_jit_L3_mean"]=HH_jit_L3_mean
df["HH_jit_L3_variance"]=HH_jit_L3_variance
df["HH_jit_L1_weight"]=HH_jit_L1_weight
df["HH_jit_L1_mean"]=HH_jit_L1_mean
df["HH_jit_L1_variance"]=HH_jit_L1_variance
df["HH_jit_L0.1_weight"]=HH_jit_L0_1_weight
df["HH_jit_L0.1_mean"]=HH_jit_L0_1_mean
df["HH_jit_L0.1_variance"]=HH_jit_L0_1_variance
df["HH_jit_L0.01_weight"]=HH_jit_L0_01_weight
df["HH_jit_L0.01_mean"]=HH_jit_L0_01_mean
df["HH_jit_L0.01_variance"]=HH_jit_L0_01_variance
df["HpHp_L5_weight"]=HpHp_L5_weight
df["HpHp_L5_mean"]=HpHp_L5_mean
df["HpHp_L5_std"]=HH_L5_std
df["HpHp_L5_magnitude"]=HpHp_L5_magnitude
df["HpHp_L5_radius"]=HpHp_L5_radius
df["HpHp_L5_covariance"]=HpHp_L5_covariance
df["HpHp_L5_pcc"]=HpHp_L5_pcc
df["HpHp_L3_weight"]=HpHp_L3_weight
df["HpHp_L3_mean"]=HpHp_L3_mean
df["HpHp_L3_std"]=HpHp_L3_std
df["HpHp_L3_magnitude"]=HpHp_L3_magnitude
df["HpHp_L3_radius"]=HpHp_L3_radius
df["HpHp_L3_covariance"]=HpHp_L3_covariance
df["HpHp_L3_pcc"]=HpHp_L3_pcc
df["HpHp_L1_weight"]=HpHp_L1_weight
df["HpHp_L1_mean"]=HpHp_L1_mean
df["HpHp_L1_std"]=HpHp_L1_std
df["HpHp_L1_magnitude"]=HpHp_L1_magnitude
df["HpHp_L1_radius"]=HpHp_L1_radius
df["HpHp_L1_covariance"]=HpHp_L1_covariance
df["HpHp_L1_pcc"]=HpHp_L1_pcc
df["HpHp_L0.1_weight"]=HpHp_L0_1_weight
df["HpHp_L0.1_mean"]=HpHp_L0_1_mean
df["HpHp_L0.1_std"]=HpHp_L0_1_std
df["HpHp_L0.1_magnitude"]=HpHp_L0_1_magnitude
df["HpHp_L0.1_radius"]=HpHp_L0_1_radius
df["HpHp_L0.1_covariance"]=HpHp_L0_1_covariance
df["HpHp_L0.1_pcc"]=HpHp_L0_1_pcc
df["HpHp_L0.01_weight"]=HpHp_L0_01_weight
df["HpHp_L0.01_mean"]=HpHp_L0_01_mean
df["HpHp_L0.01_std"]=HpHp_L0_01_std
df["HpHp_L0.01_magnitude"]=HpHp_L0_01_magnitude
df["HpHp_L0.01_radius"]=HpHp_L0_01_radius
df["HpHp_L0.01_covariance"]=HpHp_L0_01_covariance
df["HpHp_L0.01_pcc"]=HpHp_L0_01_pcc

df.to_csv('files/Data.csv')
print("df_shape : ",df.shape)
subprocess.call(['sudo','python3','predict.py'])
exit()
