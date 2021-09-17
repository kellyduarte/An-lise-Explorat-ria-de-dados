#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importando as bibliotecas:

import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('pylab', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')


# In[2]:


# Biblioteca para trabalhar com mapas:
get_ipython().system('pip install folium')


# In[3]:


# Carregando a base de dados:
dataset = pd.read_csv('2018_2_semestre.csv',sep=';',encoding='latin1')


# In[4]:


# Visualizando as 5 primeiras linhas do Dataframe:
dataset.head().T


# In[6]:


#Número de reclamações por Estado
dataset.groupby('UF')['UF'].count()


# In[7]:


#Quantidade de reclamações por sexo
dataset[u'Sexo'].value_counts()


# In[11]:


#Visulizar esse dado de forma gráfica
sns.set(style="darkgrid")
sexo = dataset[u'Sexo'].unique()
cont = dataset[u'Sexo'].value_counts()
sns.barplot(x=sexo,y=cont, hue=sexo)


# In[8]:


#Faixa etária de consumidores por sexo
dataset.groupby('Sexo')[u'Faixa Etária'].value_counts()


# In[10]:


#Para saber se consumidores mais jovens contratam mais serviçõs de internet
df2 = dataset[dataset['Como Comprou Contratou']=='Internet']
df2.groupby(u'Faixa Etária')['Como Comprou Contratou'].value_counts().plot.barh()


# In[11]:


#Para saber se esses consumidores procuram a empresa antes de registrar uma reclamação
df2 = dataset[dataset[u'Faixa Etária']=='entre 21 a 30 anos']
df2['Procurou Empresa'].value_counts().plot.barh()


# In[12]:


#Qual problema mais comum
dataset['Grupo Problema'].value_counts()


# In[13]:


#Quais são os problemas que estão relacionados a esse grupo, pois cobrança e lideraça lideram os problemas
dataset[dataset['Grupo Problema'] == u'Cobrança / Contestação'][u'Problema'].value_counts()


# In[16]:


#Qual a quantidade de reclamações por segmento de mercado
dataset[u'Segmento de Mercado'].value_counts()


# In[14]:


plt.style.use('ggplot')
plt.rcdefaults()
fig, ax = plt.subplots()

y_pos = np.arange(len(dataset['Segmento de Mercado'].value_counts()))
values = dataset['Segmento de Mercado'].value_counts()
segmentos = dataset['Segmento de Mercado'].unique()

ax.barh(y_pos, values, align='center', color='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(segmentos)
ax.invert_yaxis()
ax.set_xlabel('Reclamacoes')
ax.set_title('Reclamações por Segmento de Mercado')

plt.show()


# In[19]:


#https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html
#https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.axes.Axes.set_yticks.html
#Para ver empresas com mais reclamações
fig, ax = plt.subplots()

y_pos = np.arange(len(dataset['Nome Fantasia'].value_counts()[:20]))
values = dataset['Nome Fantasia'].value_counts()[:20]
segmentos = dataset['Nome Fantasia'].unique()[:20]

ax.barh(y_pos, values, align='center', color='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(segmentos)
ax.invert_yaxis()
ax.set_xlabel('Reclamacoes')
ax.set_title('Rank de Empresas')

plt.show()


# In[15]:


#NÃO ENTENDI AS CORRELAÇÕES
#https://pandas.pydata.org/pandas-docs/version/0.17.1/generated/pandas.core.style.Styler.background_gradient.html

#Para ver se o tempo de resposta tem alguma correlação com a nota do consumidor
#O gráfico está medindo o grau de correlação entre as variáveis.
#Onde 1 indica uma correlação perfeitamente positiva e -1 uma correlação perfeitamente negativa
#e 0 indica que não existe uma correlação entre essas variáveis.
df = dataset.drop('Total',axis=1)
corr = df.corr()
corr.style.background_gradient(cmap='coolwarm') #define o mapa


# In[16]:


#Para avaliar as notas dos consumidores
#varia entre 1 e 5, então o cliente não gostou do atendimento ou foi satisfatório
dataset.plot.density(y='Nota do Consumidor',xlim=[0,6],figsize=[6,3])


# In[17]:


#Para saber quantos dias a empresa leva para responder o cliente
#cerca de 7 a 10 dias
dataset.plot.density(y='Tempo Resposta',xlim=[0,11],figsize=[6,3])


# In[18]:


#Proporção de reclamações registradas e não respondidas

x = dataset.groupby(u'Segmento de Mercado')[u'Segmento de Mercado'].count()

#Filtrando os segmentos de mercado com mais de 20 reclamações
x = x[x > 20]

df = dataset[dataset[u'Segmento de Mercado'].isin(x.keys())]
df = df[df[u'Avaliação Reclamação']==u'Não Resolvida']
x1 = df.groupby(u'Segmento de Mercado')[u'Segmento de Mercado'].count()
x1


# In[19]:


# Gráfico:
sns.set(style="whitegrid")

f, ax = plt.subplots(figsize=(8, 10))

sns.set_color_codes("pastel")
sns.barplot(x=x.values, y=x.keys(), label="Total de reclamacoes", color="b")

sns.set_color_codes("muted")
sns.barplot(x=x1.values, y=x1.keys(),label="Reclamacoes nao resolvidas", color="r")

ax.legend(ncol=2, loc="lower right", frameon=True)
ax.set(ylabel="", xlabel="Reclamacoes e suas situacoes")
sns.despine(left=False, bottom=True)


# In[ ]:




