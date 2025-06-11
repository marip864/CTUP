<h1 align='center'>
  CTUP: Facilitando os cálculos termodinâmicos</a>
</h1>
<p align="center"> Este projeto é uma calculadora simples para transformações termodinâmicas. Ela pode calcular calor, trabalho, variação da energia interna e da entropia em um gás monoatômico ideal a partir de uma sequência de pontos, cada um com pressão, volume e temperatura determinados. Além disso, ela retorna um gráfico P x V das transformações.</p>

<img loading="lazy" src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/>  [![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try) 

Calculadora Termodinâmica usando Python.
  A calculadora admite apenas transformações isotérmicas, isométricas, isobáricas ou adiabáticas. As limitações de operações com float no Python podem ocasionar pequenos erros. Para evitar isso, o programa assume que qualquer transformação em que P, V e T mudam é adiabática reversível.