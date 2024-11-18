# Dance Hall Simulation

## Descripción

El **Dance Hall Simulation** es un modelo de sistemas multiagente desarrollado en Python con el framework [Mesa](https://mesa.readthedocs.io/). Este modelo simula un salón de baile donde los agentes, representados como bailarines, interactúan entre sí formando parejas, bailando, cansándose y descansando.

Los bailarines se mueven dentro de un espacio discreto, alternando entre la pista de baile (centro) y las áreas de descanso (bordes). Su comportamiento está guiado por reglas específicas que definen cómo buscan pareja, bailan, se cansan y recuperan energía.


## Comportamiento de los Agentes

### Estados de los Bailarines
1. **Soltero (`soltero`)**:
   - Los bailarines buscan pareja en su vecindad inmediata.
   - Si no encuentran pareja, se mueven aleatoriamente dentro de la pista de baile.

2. **Emparejado (`emparejado`)**:
   - Bailan juntos, perdiendo energía con cada paso.
   - Si la energía de uno de los bailarines se agota, ambos se separan y vuelven al estado de `soltero` o `cansado`.

3. **Cansado (`cansado`)**:
   - Se mueven hacia los bordes del salón para descansar.
   - Permanecen en este estado por un período determinado antes de recuperar su energía y regresar al estado de `soltero`.


## Espacio del Modelo

- **Tamaño del espacio**: Un grid bidimensional discreto de tamaño ajustable (por defecto, 10x10).
- **Pista de baile**: El área central del grid.
- **Zonas de descanso**: Las celdas en los bordes del grid.


## Parámetros Ajustables

El modelo incluye parámetros configurables a través de un slider en la visualización:

- **Número de bailarines (`num_dancers`)**: Número de agentes en la simulación (10-50, por defecto 20).
- **Dimensiones del salón (`width`, `height`)**: Ancho y alto del espacio de simulación.


## Reglas de Interacción

1. **Buscar pareja**:
   - Los agentes en estado `soltero` buscan a otros agentes `soltero` en las celdas vecinas.
   - Si encuentran una pareja, ambos pasan al estado `emparejado`.

2. **Bailar**:
   - Los agentes emparejados pierden energía mientras bailan.
   - Si un agente se queda sin energía, ambos dejan de bailar. El agente agotado pasa al estado `cansado` y su pareja regresa a `soltero`.

3. **Descansar**:
   - Los agentes cansados se mueven a los bordes del salón.
   - Permanecen en este estado hasta recuperar suficiente energía para volver al estado `soltero`.


## Métricas Colectadas

El modelo recopila las siguientes estadísticas durante la simulación:

- **Parejas formadas**: El número total de parejas activas en cada paso.
- **Bailarines cansados**: La cantidad de agentes en estado `cansado`.
- **Energía promedio**: Energía promedio de los bailarines a lo largo del tiempo (puede añadirse si es útil).



## Visualización

El modelo incluye una visualización interactiva con los siguientes componentes:

1. **Canvas Grid**:
   - Representa la posición y el estado de cada bailarín:
     - **Azul**: Solteros.
     - **Verde**: Emparejados.
     - **Rojo**: Cansados.

2. **Gráfica de Métricas**:
   - Muestra el número de parejas formadas y bailarines cansados a lo largo del tiempo.


## Instrucciones de Ejecución

1. Clona el repositorio o descarga los archivos del proyecto.
2. Asegúrate de tener un entorno virtual con las dependencias instaladas:
   ```bash
   pip install mesa
   ```
3. Ejecuta el servidor de visualización:
   ```bash
   python server.py
   ```
4. Abre tu navegador en `http://127.0.0.1:8521/`.



## Ejemplo de Simulación

1. Ajusta el número de bailarines usando el slider.
2. Observa cómo los agentes interactúan en la pista de baile y las áreas de descanso.
3. Analiza las métricas en la gráfica para identificar tendencias en el comportamiento colectivo.

