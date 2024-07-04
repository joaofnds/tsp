# Execuções

## Nearest Neighbor

Complexidade: O(n^2) \
O(log n)-aproximado

### 253 - 11x11

Time (mean ± σ): 21.5 ms ± 1.4 ms \
Range (min … max): 19.2 ms … 25.4 ms \
113 runs

Cost: 299 \
Absolute Error: 46 \
Relative Error: 18.18%

### 1194 - 15x15

Time (mean ± σ): 22.4 ms ± 1.6 ms \
Range (min … max): 18.2 ms … 27.8 ms \
123 runs

Cost: 1260 \
Absolute Error: 66 \
Relative Error: 5.53%

### 1248 - 6x6

Time (mean ± σ): 23.0 ms ± 1.8 ms \
Range (min … max): 19.3 ms … 28.3 ms \
119 runs

Cost: 1272 \
Absolute Error: 24 \
Relative Error: 1.92%

### 7013 - 44x44

Time (mean ± σ): 23.0 ms ± 1.8 ms \
Range (min … max): 19.4 ms … 27.6 ms \
120 runs

Cost: 10587 \
Absolute Error: 3,574 \
Relative Error: 50.96%

### 27603 - 29x29

Time (mean ± σ): 22.8 ms ± 1.6 ms \
Range (min … max): 18.9 ms … 28.2 ms \
118 runs

Cost: 36399 \
Absolute Error: 8796 \
Relative Error: 31.87%

## Held Karp

Complexidade: O(2^n \* n^2)

- 2^n para as possíveis combinações de cidades
- n^2 para calcular o custo de cada combinação

explorou ~70k combinações por segundo na minha máquina

## 253 - 11x11

Time (mean ± σ): 26.9 ms ± 1.2 ms \
Range (min … max): 24.2 ms … 29.9 ms \
95 runs

## 1194 - 15x15

Time (mean ± σ): 155.8 ms ± 2.1 ms \
Range (min … max): 150.4 ms … 160.0 ms \
19 runs

## 1248 - 6x6

Time (mean ± σ): 23.7 ms ± 1.8 ms \
Range (min … max): 19.8 ms … 30.3 ms \
118 runs

## 7013 - 44x44

levaria ~(2^44/70k) segundos pra rodar (~8 anos)

## held_karp 27603 - 29x29

levaria ~(2^29/70k) segundos pra rodar (~2 horas)
