# Perceptron

Implementação de um perceptron de camada única.

## Instalação

Use o [pip](https://pip.pypa.io/en/stable/) para instalar as dependências.

```bash
pip install -r requirements.txt
```

## Usage

```python
# Inicialização da classe Perceptron
ppn = Perceptron(eta=0.1, n_iter=10)
# chamada do método fit com as entradas de sources.iris
ppn.fit(X, y)
```


## License

[MIT](https://choosealicense.com/licenses/mit/)