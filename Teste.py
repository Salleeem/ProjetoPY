import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yaml

# Carregar dados do arquivo YAML
with open('Dados.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Criar DataFrame a partir dos dados
df = pd.DataFrame(data)

# Visualizar os dados
print(df)
print()

# Visualização inicial
print("Leitura e Visualização Inicial:")
print(df.head())
print()

# Gráfico de barras para contagem de vendas por mês
df['Data da Compra'] = pd.to_datetime(df['Data da Compra'])
df['Mês'] = df['Data da Compra'].dt.month
plt.figure(figsize=(8, 4))
sns.countplot(x='Mês', data=df)
plt.title('Contagem de Vendas por Mês')
plt.xlabel('Mês')
plt.ylabel('Contagem de Vendas')
plt.show()
print()

# Análise Estatística Inicial
print("Análise Estatística Inicial:")
print(df.describe())
print()

# Verificação de valores ausentes
print("Verificação de valores ausentes:")
print(df.isnull().sum())
print()

# Análise de Produtos
print("Análise de Produtos:")
# Produtos mais vendidos
produtos_mais_vendidos = df['Produto'].value_counts().reset_index()
produtos_mais_vendidos.columns = ['Produto', 'Quantidade']

plt.figure(figsize=(10,6))
sns.barplot(x='Produto', y='Quantidade', data=produtos_mais_vendidos)
plt.title('Produtos Mais Vendidos')
plt.xlabel('Produto')
plt.ylabel('Quantidade Vendida')
plt.xticks()
plt.show()
print()

# Receita total gerada por produto
receita_por_produto = df.groupby('Produto')['Preco'].sum().reset_index()
plt.figure(figsize=(8, 8))
plt.pie(receita_por_produto['Preco'], labels=receita_por_produto['Produto'], autopct='%1.1f%%', startangle=140)
plt.title('Distribuição da Receita por Produto')
plt.axis('equal')
plt.show()
print()

# Análise Temporal
print("Análise Temporal:")
# Evolução das vendas ao longo do tempo
vendas_por_data = df.groupby(df['Data da Compra'].dt.to_period('M')).size()
plt.figure(figsize=(10, 6))
vendas_por_data.plot(marker='o')
plt.title('Evolução das Vendas ao Longo do Tempo')
plt.xlabel('Data da Compra')
plt.ylabel('Quantidade de Vendas')
plt.xticks()
plt.grid(True)
plt.show()
print()

# Análise de Cliente
print("Análise de Cliente:")
# Valor total gasto por cliente
valor_total_por_cliente = df.groupby('ID do Cliente')['Preco'].sum().reset_index()
plt.figure(figsize=(10, 6))
sns.histplot(valor_total_por_cliente['Preco'], bins=5, kde=True)
plt.title('Distribuição dos Gastos dos Clientes')
plt.xlabel('Valor Total Gasto')
plt.ylabel('Frequência')
plt.show()
print()

# Clientes mais fiéis
frequencia_compras_por_cliente = df['ID do Cliente'].value_counts().reset_index()
frequencia_compras_por_cliente.columns = ['ID do Cliente', 'Frequência de Compras']
# Adicionando a coluna 'Preco' ao DataFrame valor_total_por_cliente
valor_total_por_cliente['Preco'] = df.groupby('ID do Cliente')['Preco'].sum().values
valor_fiel_por_cliente = pd.merge(valor_total_por_cliente, frequencia_compras_por_cliente, on='ID do Cliente')
plt.figure(figsize=(10, 6))
plt.scatter(valor_fiel_por_cliente['Frequência de Compras'], valor_fiel_por_cliente['Preco'])
plt.title('Valor Total Gasto vs Frequência de Compras')
plt.xlabel('Frequência de Compras')
plt.ylabel('Valor Total Gasto')
plt.show()
print()

# Análise de Preços
print("Análise de Preços:")
# Distribuição de preços dos produtos
plt.figure(figsize=(8, 6))
sns.boxplot(x='Produto', y='Preco', data=df)
plt.title('Distribuição de Preços dos Produtos')
plt.xlabel('Produto')
plt.ylabel('Preço')
plt.xticks()
plt.show()
print()

# Preço médio dos produtos
Preco_medio = df.groupby('Produto')['Preco'].mean()
print("Preço Médio dos Produtos:")
print(Preco_medio)
print()


# Visualização Avançada
print("Visualização Avançada:")

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Frequência de Compras', y='Preco', data=valor_fiel_por_cliente)
plt.title('Valor Total Gasto vs Frequência de Compras por Cliente')
plt.xlabel('Frequência de Compras')
plt.ylabel('Valor Total Gasto')
plt.show()



