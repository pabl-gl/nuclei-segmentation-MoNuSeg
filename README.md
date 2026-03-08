# 🧬 Nuclei Segmentation — VA Practice 2

---

## Contexto del proyecto

Este repositorio corresponde a la **Práctica 2 de la asignatura de Visión Artificial** y aborda el análisis de un conjunto de **imágenes histológicas teñidas con hematoxilina**, en las que se observan **núcleos celulares** con una elevada variabilidad morfológica.

El problema estudiado es representativo de escenarios reales en histopatología, donde las estructuras de interés presentan diferencias significativas en **tamaño**, **forma** y **grado de contacto**, lo que dificulta su segmentación automática.

---

## Base de datos

La base de datos está formada por un conjunto de imágenes histológicas acompañadas de sus correspondientes **segmentaciones de referencia (*ground truth*)**, que delimitan manualmente los núcleos celulares presentes en cada imagen.

Las imágenes incluyen distintos regímenes morfológicos, entre los que se encuentran:

- Núcleos pequeños, compactos y bien separados  
- Núcleos de mayor tamaño, irregulares y frecuentemente en contacto  
- Escenarios mixtos con alta heterogeneidad estructural  

Esta diversidad permite evaluar el comportamiento de los métodos de segmentación frente a condiciones visuales muy distintas.

---

## Problema abordado

A partir de las imágenes proporcionadas, el objetivo del proyecto es:

- Identificar correctamente las **regiones nucleares**
- Separar **núcleos individuales** cuando aparecen en contacto
- Extraer información cuantitativa relevante a partir de la segmentación
- Comparar los resultados obtenidos con el *ground truth* disponible

El enfoque del trabajo pone el acento en el análisis del problema y en la comprensión de las dificultades inherentes a la segmentación de estructuras biológicas.

---

## Enfoque general

El proyecto se plantea como un estudio práctico del uso de **técnicas clásicas de Visión Artificial** aplicadas a imágenes histológicas, con el objetivo de analizar sus capacidades y limitaciones ante conjuntos de datos con alta variabilidad morfológica.

---

