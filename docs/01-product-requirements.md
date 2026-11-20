# Documento de requisitos del producto (PRD)

## 1. Visión del producto

Desarrollar un asistente educativo conversacional basado en Amazon Bedrock que facilite el aprendizaje personalizado de conceptos relacionados con modelos de lenguaje de gran tamaño (LLMs) y Retrieval-Augmented Generation (RAG), permitiendo a estudiantes principiantes e intermedios interactuar con diferentes perfiles de expertos en una interfaz accesible, intuitiva y adaptable a sus necesidades de aprendizaje.

## 2. Problema y objetivo

La institución educativa busca ofrecer a sus estudiantes una herramienta complementaria para comprender conceptos de RAG y LLMs mediante preguntas en lenguaje natural y explicaciones contextualizadas.

**Objetivo:** facilitar el aprendizaje de estos conceptos mediante una experiencia conversacional que ajuste la profundidad de las respuestas según el contexto y las solicitudes del estudiante, sin requerir una clasificación explícita de su nivel.

## 3. Stakeholders

| Stakeholder | Interés o necesidad |
|---|---|
| Institución educativa | Ofrecer una herramienta de apoyo al aprendizaje. |
| Estudiantes | Comprender RAG y LLMs mediante explicaciones personalizadas. |
| Desarrollador | Construir, documentar y mantener la solución. |

## 4. Requisitos funcionales

| ID | Requisito | Prioridad |
|---|---|---|
| RF01 | Permitir seleccionar uno de tres perfiles predefinidos: Profesor de IA, Arquitecto AWS y Entrenador de certificación. | Alta |
| RF02 | Permitir enviar preguntas mediante una interfaz conversacional. | Alta |
| RF03 | Generar respuestas utilizando un modelo fundacional disponible en Amazon Bedrock. | Alta |
| RF04 | Mantener el historial de conversación durante la sesión activa. | Alta |
| RF05 | Adaptar el estilo de respuesta al perfil seleccionado y ajustar la profundidad de las explicaciones según el contexto conversacional y las solicitudes del estudiante, sin un selector de nivel. | Alta |
| RF06 | Permitir iniciar una nueva conversación limpiando el historial. | Alta |
| RF07 | Mostrar un indicador de procesamiento mientras se genera una respuesta. | Media |
| RF08 | Gestionar y comunicar errores de conexión, permisos o autenticación con AWS sin exponer credenciales. | Alta |
| RF09 | Mostrar un mensaje inicial con instrucciones de uso. | Media |
| RF10 | Centralizar las instrucciones de los tres perfiles en archivos o módulos de configuración de prompts, separados de la interfaz y de la integración con Bedrock. | Alta |

## 5. Requisitos no funcionales

| ID | Requisito | Criterio |
|---|---|---|
| RNF01 | Portabilidad | La aplicación podrá ejecutarse localmente mediante Docker. |
| RNF02 | Usabilidad | La interfaz será clara y estará construida con Streamlit. |
| RNF03 | Seguridad | Las credenciales AWS no estarán incrustadas en el código fuente ni publicadas en el repositorio. |
| RNF04 | Mantenibilidad | El código Python estará organizado en módulos con responsabilidades separadas. |
| RNF05 | Rendimiento percibido | La interfaz mostrará retroalimentación visual mientras espera la respuesta del modelo. |
| RNF06 | Compatibilidad | La aplicación será accesible desde navegadores modernos. |
| RNF07 | Configurabilidad | La región AWS y el identificador del modelo serán configurables sin modificar la lógica principal. |
| RNF08 | Privacidad de sesión | El historial conversacional se mantendrá en memoria de la sesión de Streamlit y no se guardará en una base de datos de la aplicación. |

## 6. Criterios de éxito

| Indicador | Criterio de aceptación |
|---|---|
| Funcionamiento | Un estudiante puede enviar una pregunta y recibir una respuesta del modelo a través de Bedrock. |
| Personalización por perfil | Los tres perfiles ofrecen enfoques diferenciados ante una misma pregunta. |
| Adaptación conversacional | Ante una solicitud como «explícalo de manera más sencilla», el asistente reformula la explicación sin exigir seleccionar un nivel. |
| Continuidad | El asistente responde preguntas de seguimiento teniendo en cuenta el historial de la sesión. |
| Gestión de sesión | El estudiante puede limpiar el historial e iniciar una nueva conversación. |
| Portabilidad | La aplicación se inicia con Docker siguiendo las instrucciones del repositorio. |
| Seguridad | El repositorio no contiene credenciales reales de AWS. |
| Usabilidad | El estudiante puede seleccionar un perfil e iniciar una conversación desde la interfaz. |
| Gestión de prompts | Las instrucciones de cada perfil pueden modificarse en su configuración sin editar la lógica de conexión a Bedrock. |

## 7. Decisiones de producto

- La aplicación ofrecerá tres perfiles de experto predefinidos y seleccionables.
- No se solicitará al estudiante que declare un nivel de conocimiento.
- La profundidad de las explicaciones se ajustará mediante el contexto de la conversación y las solicitudes del estudiante.
- Las instrucciones de los perfiles estarán separadas del código de interfaz y de acceso a AWS.
- La conversación se conservará únicamente durante la sesión activa de la aplicación.
