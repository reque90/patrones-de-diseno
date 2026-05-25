# Trabajo: Patrones de diseño

## 1) Objetivo

### ¿Qué son los patrones de diseño?
Los **patrones de diseño** son soluciones reutilizables a problemas frecuentes que aparecen al diseñar software orientado a objetos. No son código cerrado ni librerías, sino **plantillas de solución** que se adaptan al contexto.

### ¿Cuándo se usan?
Se usan cuando en el diseño aparecen problemas repetitivos, por ejemplo:
- Crear objetos complejos sin acoplar el código a clases concretas.
- Cambiar comportamientos en tiempo de ejecución.
- Comunicar objetos entre sí sin dependencias rígidas.
- Organizar responsabilidades para facilitar mantenimiento.

### ¿Por qué son útiles?
- Reducen acoplamiento entre componentes.
- Mejoran mantenibilidad y extensibilidad.
- Facilitan reutilización de ideas probadas.
- Mejoran la comunicación entre desarrolladores (lenguaje común: “usemos Strategy”, “esto pide Factory Method”, etc.).

### ¿Diseño, arquitectura o microarquitectura?
Los patrones de diseño se sitúan principalmente en la **microarquitectura** del software (estructura interna de clases/objetos y sus colaboraciones).

Relación con otros niveles:
- **Arquitectura**: define la estructura global (capas, servicios, bounded contexts, etc.).
- **Diseño (de componentes/módulos)**: concreta responsabilidades y relaciones dentro de partes del sistema.
- **Microarquitectura**: aquí viven los patrones GoF clásicos (Factory, Strategy, Observer, etc.).

En resumen: no sustituyen la arquitectura, pero sí la **materializan** dentro del código.

---

## 2) Patrones elegidos e implementación en Python

He elegido:
1. **Creacional**: `Factory Method`
2. **De comportamiento**: `Strategy`

Se incluyen **dos ejemplos diferentes de cada patrón**.

---

## Patrón creacional: Factory Method

### Idea
Define una interfaz para crear objetos, pero permite que subclases o fábricas concretas decidan qué clase concreta instanciar.

### Cuándo usarlo
- Cuando el código cliente no debe depender de clases concretas.
- Cuando quieres abrir la creación a nuevas variantes sin tocar el cliente (principio abierto/cerrado).

### Ejemplo 1: Notificaciones (`python/factory_notifications.py`)
- Productos: `EmailNotification`, `SMSNotification`.
- Fábricas: `EmailFactory`, `SMSFactory`.
- Cliente: trabaja contra la abstracción `NotificationFactory`.

### Ejemplo 2: Exportadores de reportes (`python/factory_exporters.py`)
- Productos: `PDFExporter`, `CSVExporter`.
- Fábricas: `PDFExporterFactory`, `CSVExporterFactory`.
- Cliente: genera salida sin conocer la clase concreta.

---

## Patrón de comportamiento: Strategy

### Idea
Encapsula algoritmos intercambiables detrás de una misma interfaz y permite cambiar el comportamiento dinámicamente.

### Cuándo usarlo
- Cuando existen varias formas de resolver la misma tarea.
- Cuando hay muchos `if/elif` para elegir algoritmo.
- Cuando quieres cambiar comportamiento en tiempo de ejecución.

### Ejemplo 1: Descuentos en e-commerce (`python/strategy_discounts.py`)
- Estrategias: `NoDiscount`, `PercentageDiscount`, `FixedDiscount`.
- Contexto: `Checkout`.
- Cambio dinámico de estrategia según campaña o tipo de cliente.

### Ejemplo 2: Rutas de navegación (`python/strategy_routes.py`)
- Estrategias: `CarRouteStrategy`, `BikeRouteStrategy`, `WalkRouteStrategy`.
- Contexto: `Navigator`.
- Permite cambiar algoritmo de ruta según medio de transporte.

---

## Cómo ejecutar

Desde la raíz del proyecto:

```bash
python3 python/factory_notifications.py
python3 python/factory_exporters.py
python3 python/strategy_discounts.py
python3 python/strategy_routes.py
```

---

## Conclusión

Los patrones de diseño ayudan a construir software más flexible y mantenible. En este trabajo:
- `Factory Method` desacopla la creación de objetos de su uso.
- `Strategy` desacopla el comportamiento de quien lo consume.

Ambos patrones muestran cómo decisiones de **microarquitectura** mejoran la calidad del diseño y facilitan evolución del sistema.
