import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Carregar dados
df = pd.read_csv('leads.csv')

# Selecionar features
X = df[['tempo_navegacao_site', 'paginas_visitadas', 'setor_empresa', 'cidade_lead']]
y = df['converteu']  # ou a coluna alvo que você definiu

# Pré-processamento (ex: one-hot encoding)
X = pd.get_dummies(X)

# Dividir dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar modelo
model = LogisticRegression()
model.fit(X_train, y_train)

# Avaliar
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
