## 🎮🕹️ ESQUIVA Y GANA

Un juego simple creado con Python y su libreria Pygame. Se trata de esquivar obstáculos en el que controlas un personaje de color que se mueve horizontalmente en la parte inferior de la pantalla. El objetivo es evitar que los "cubos blancos" (enemigos) que caen desde la parte superior de la pantalla colisionen con tu personaje. El juego tiene varias características clave:

- **Menú Principal**: El juego comienza con un menú principal que permite al jugador elegir el color del personaje, la dificultad y la intensidad del juego.

- **Elección de Color**: Puedes seleccionar el color del personaje entre rojo, verde o azul.

- **Dificultad**: Puedes elegir entre tres niveles de dificultad: fácil, medio y difícil.

- **Intensidad**: Puedes ajustar la intensidad del juego en tres niveles: baja, media y alta.

- **Juego en Sí**: Una vez que seleccionas las opciones del menú principal y presionas la barra espaciadora, el juego comienza. Los cubos blancos (enemigos) comienzan a caer desde la parte superior de la pantalla, y debes esquivarlos moviendo tu personaje de izquierda a derecha.

- **Puntuación**: El juego lleva un registro de tu puntuación, que aumenta a medida que esquivas los enemigos.

- **Pantalla de Game Over**: El juego termina cuando tu personaje choca con un enemigo. Se muestra una pantalla de "Game Over" y puedes volver al menú principal para intentarlo de nuevo.

- **Condición de Victoria**: Hay una condición de victoria en la que debes alcanzar 30 puntos para ganar el juego.

En resumen, el juego se centra en la habilidad del jugador para esquivar enemigos que caen y recolectar puntos mientras se enfrenta a diferentes niveles de dificultad e intensidad. El objetivo es obtener la puntuación más alta posible y disfrutar de un desafío divertido.

## 🔌 INSTALAR JUEGO

Clonar el repositorio.

```bash
  git clone https://github.com/kevinserrano01/esquiva_y_gana.git
```

Acceder a la carpeta principal que se crea luego de clonar el repositorio.

```bash
  cd esquiva_y_gana
```

Crear un entorno virtual

```bash
  py -m venv env
```

Activar el entorno

```bash
  cd env/Script/activate
```

Posicionarse en la carpeta principal e instalar las dependencias.

```bash
  pip install -r requirements.txt
```
Ejecutar el archivo "app.py" para abrir el juego.

```bash
  py main.py
```