# Turtle (1)

[Link](https://realpython.com/beginners-guide-python-turtle/#drawing-a-shape)

## Turtle Commands

### Getting Started

- To import

```python
import turtle
```

- Get Screen

```python
s = turtle.getscreen()
```

- Initialize Variable of Usage (Pencil), in this case, we’ll use “t” as variable name

```python
t = turtle.Turtle()
```

### Design Characteristics

- Changing the screen color

```python
turtle.bgcolor("blue")
```

- Changing the screen title

```python
turtle.title("My Turtle Program")
```

- Changing the pensize

```python
t.pensize(5)
```

- Changing the turtle´s appearance
    - Size
    
    ```python
    t.shapesize(2)
    ```
    
    - Color
    
    ```python
    t.pencolor("green")
    ```
    
    - Shape
    
    ```python
    t.shape("circle")
    ```
    
    - Available Shapes
        - Square
        - Arrow
        - Circle
        - Turtle
        - Triangle
        - Classic
- Pen Speed

```python
t.speed(10)
```

### **Moving the Turtle**

There are four directions that a turtle can move in:

- Forward

- Backward

- Left

- Right

```python
t.right(90)
t.forward(100)
t.left(90)
t.backward(100)
t.left(90)
t.forward(100)
t.right(90)
t.forward(100)
```

Or it can be shortened

- Fd

- Bk

- Lt

- Rt

```python
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
```

The command goes like

<aside>
🐢 Variable Name + . + Direction + Distance or Angle

</aside>

### **Drawing Preset Figures**

- Circle

- Dot

```python
t.circle(60)
```

```python
t.dot(20)
```

### Filling a Shape

To fill a shape you need to follow this steps after setting the screen and pencilç

1. Write the command for begging a fill
2. Write the shape code
3. Write the command to end the fill

**Commands**

- `t.beginfill()`

- `t.endfill()`

```python
t.pencolor("purple")
t.fillcolor("orange")
t.pensize(10)
t.speed(9)
t.begin_fill()
t.circle(90)
t.end_fill()
```

### Changing Pen Characteristics in One Line

```python
t.pen(pencolor="purple", fillcolor="orange", pensize=10, speed=9)
t.begin_fill()
t.circle(90)
t.end_fill()
```

### Pen Up and Pen Down

Sometimes, you may want to move your turtle to another point on the screen without drawing anything on the screen itself. To do this, you use `.penup()`. Then, when you want to start drawing again, you use `.pendown()`

```python
t.fd(100)
t.rt(90)
t.penup()
t.fd(100)
t.rt(90)
t.pendown()
t.fd(100)
t.rt(90)
t.penup()
t.fd(100)
t.pendown()
```
