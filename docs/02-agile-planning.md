# Planificación del proyecto

## 1. Objetivo de la planificación

Organizar la construcción de un asistente conversacional que ayude a estudiantes a comprender RAG y LLMs a través de tres perfiles de experto, respuestas de Amazon Bedrock y continuidad conversacional durante una sesión. El producto no exige al estudiante declarar su nivel: la profundidad de las explicaciones responde al contexto y a sus solicitudes.

## 2. Organización del trabajo

| Elemento | Acuerdo |
|---|---|
| Desarrollo | Responsable del proyecto: diseña, implementa, verifica y documenta. |
| Unidad de trabajo | Historia de usuario verificable y tareas técnicas asociadas. |

## 3. Product Backlog priorizado

| ID | Historia de usuario | Prioridad | Requisitos relacionados | Sprint previsto |
|---|---|---|---|---|
| US01 | Como estudiante, quiero seleccionar uno de tres perfiles de experto para aprender desde el enfoque que prefiera. | Alta | RF-01, RF-05 | 1 |
| US02 | Como estudiante, quiero escribir preguntas y obtener respuestas para resolver dudas sobre RAG y LLMs. | Alta | RF-02, RF-03 | 2 |
| US03 | Como estudiante, quiero hacer preguntas de seguimiento para continuar aprendiendo sin repetir el contexto. | Alta | RF-04 | 2 |
| US04 | Como estudiante, quiero pedir explicaciones más simples o más técnicas para ajustar el aprendizaje a mis necesidades. | Alta | RF-05 | 2 |
| US05 | Como estudiante, quiero reiniciar la conversación para comenzar un tema nuevo sin arrastrar el contexto anterior. | Alta | RF-06 | 1–2 |
| US06 | Como estudiante, quiero saber que mi pregunta se está procesando para comprender el estado de la aplicación. | Media | RF-07 | 1–2 |
| US07 | Como estudiante, quiero recibir mensajes comprensibles cuando falle el servicio para saber qué ha ocurrido y cómo proceder. | Alta | RF-08 | 2 |
| US08 | Como estudiante, quiero ver instrucciones iniciales para comenzar a utilizar el asistente sin asistencia adicional. | Media | RF-09 | 1 |
| US09 | Como responsable técnico, quiero mantener las instrucciones de los perfiles separadas del código de integración para modificarlas sin alterar la conexión con AWS. | Alta | RF-10, RNF-04 | 2 |
| US10 | Como responsable técnico, quiero ejecutar el asistente mediante Docker con configuración externa para facilitar su instalación local. | Alta | RNF-01, RNF-03, RNF-07 | 3 |

### 3.1 Criterios de aceptación por historia

**US-01 — Selección de perfil**
- La interfaz ofrece exactamente tres perfiles: Profesor de IA, Arquitecto AWS y Entrenador de certificación.
- El estudiante puede identificar el perfil activo antes de enviar preguntas.
- No se solicita elegir entre nivel principiante o intermedio.

**US-02 — Preguntas y respuestas**
- El estudiante puede enviar texto desde el chat.
- La aplicación envía la solicitud al modelo configurado mediante Amazon Bedrock.
- La respuesta recibida se visualiza como mensaje del asistente.

**US-03 — Historial contextual**
- Los mensajes previos de la sesión se muestran en orden cronológico.
- Una pregunta de seguimiento utiliza el contexto disponible de esa conversación.
- El historial no persiste en una base de datos al finalizar la sesión.

**US-04 — Adaptación conversacional**
- Ante «explícalo de forma más sencilla», la respuesta reformula la explicación previa con menor complejidad.
- Ante «profundiza con un ejemplo técnico», ofrece mayor detalle dentro del tema.
- La adaptación no depende de declarar previamente un nivel.

**US-05 — Reinicio**
- Existe un control visible para iniciar una conversación nueva.
- Su uso elimina los mensajes anteriores de la sesión activa y muestra el estado inicial.

**US-06 — Estado de procesamiento**
- Mientras se espera la respuesta, aparece una señal visible de procesamiento.
- La señal desaparece al finalizar la respuesta o producirse un error.

**US-07 — Errores**
- Los fallos de permisos, autenticación, conexión o configuración muestran un mensaje comprensible.
- Los mensajes visibles y los registros no exponen claves ni secretos.
- Un error no provoca la caída de toda la interfaz.

**US-08 — Bienvenida**
- Al iniciar una conversación vacía se presentan el propósito del asistente y una indicación breve para comenzar.

**US-09 — Gestión de prompts**
- Cada perfil tiene instrucciones identificables en un archivo o módulo de prompts.
- La selección de perfil determina qué instrucciones se envían al modelo.
- Modificar el texto de un perfil no exige cambiar el módulo de comunicación con Bedrock.

**US-10 — Ejecución local**
- Existe un `Dockerfile` funcional y un procedimiento reproducible para construir e iniciar la imagen.
- La región y el identificador del modelo pueden configurarse externamente.
- Las credenciales se suministran de forma externa y segura, sin incluirse en la imagen ni en el repositorio.
- La interfaz puede abrirse desde el navegador en el puerto documentado, con conexión a AWS disponible.

## 4. Sprint Backlogs

### Sprint 1 — Experiencia e interfaz

**Objetivo:** disponer de una interfaz navegable que permita elegir un perfil, visualizar el estado inicial y gestionar una conversación simulada.

| ID tarea | Actividad | Relación |
|---|---|---|
| T1.1 | Diseñar flujo y wireframe del chat y selector de perfiles en Figma. | US-01, US-08 |
| T1.2 | Inicializar proyecto Python y dependencias de Streamlit. | Base técnica |
| T1.3 | Crear pantalla de chat, selector de perfil y bienvenida. | US-01, US-08 |
| T1.4 | Añadir mensajes simulados y control de reinicio para validar la interfaz. | US-05 |
| T1.5 | Mostrar indicador de procesamiento durante la simulación. | US-06 |

**Demostración de cierre:** una persona puede abrir la aplicación, elegir un perfil, escribir un mensaje de prueba, ver una respuesta simulada y reiniciar el chat.

### Sprint 2 — Integración e inteligencia conversacional

**Objetivo:** reemplazar la simulación por respuestas reales de Bedrock, manteniendo el contexto y el comportamiento de cada perfil.

| ID tarea | Actividad | Relación |
|---|---|---|
| T2.1 | Configurar Boto3, región, identificador del modelo y autenticación local. | US-02 |
| T2.2 | Implementar un módulo de cliente Bedrock con la API de conversación compatible. | US-02 |
| T2.3 | Crear módulo de prompts con las instrucciones de los tres perfiles. | US-09 |
| T2.4 | Integrar el historial mediante `st.session_state` y pasarlo al modelo. | US-03 |
| T2.5 | Verificar respuestas de seguimiento y reformulaciones simples/técnicas. | US-04 |
| T2.6 | Gestionar indicadores de espera y errores sin exponer información sensible. | US-06, US-07 |
| T2.7 | Probar las tres variantes de perfil con una misma pregunta. | US-01, US-09 |

**Demostración de cierre:** el usuarii conversa con Bedrock, pide aclaraciones contextualizadas y recibe diferentes enfoques según el perfil.

### Sprint 3 — Calidad, Docker y entrega

**Objetivo:** lograr una ejecución local reproducible, comprobar los principales escenarios y dejar el proyecto preparado para GitHub.

| ID tarea | Actividad | Relación |
|---|---|---|
| T3.1 | Crear `Dockerfile` y `.dockerignore`. | US-10 |
| T3.2 | Crear `.env.example`, `.gitignore` y guía de configuración sin secretos. | US-10 |
| T3.3 | Construir e iniciar el contenedor y verificar acceso a Streamlit. | US-10 |
| T3.4 | Ejecutar pruebas funcionales y de errores con evidencias breves. | Todas |
| T3.5 | Actualizar README con objetivo, arquitectura, requisitos y comandos de ejecución. | Entrega |
| T3.6 | Revisar archivos a publicar y preparar el repositorio GitHub. | Seguridad y entrega |

## 5. Definition of Done (DoD)

Una historia se marca **Terminada** cuando:

1. Cumple sus criterios de aceptación verificables.
2. Su funcionamiento ha sido probado manualmente; se registran los casos relevantes.
3. No contiene credenciales reales ni secretos en código, configuración versionada o mensajes de error.
4. Sigue la separación prevista entre interfaz, prompts y acceso a Bedrock.
5. No presenta fallos conocidos que impidan el flujo principal asociado.
6. Los cambios relevantes están reflejados en el README o en `docs/`.
7. El responsable revisa el resultado y lo acepta.

Para declarar **completado el proyecto**, además debe poder construirse y ejecutarse el contenedor y deben superarse los criterios de éxito del PRD.

## 6. Matriz mínima de pruebas

| ID | Escenario | Resultado esperado | Historias |
|---|---|---|---|
| CP01 | Elegir cada uno de los tres perfiles. | El perfil activo queda identificado y condiciona las respuestas. | US-01, US-09 |
| CP02 | Preguntar «¿Qué es RAG?». | Se recibe respuesta de Bedrock y se muestra en el chat. | US-02 |
| CP03 | Preguntar «¿En qué se diferencia de fine-tuning?» después de CP-02. | La respuesta conserva el contexto de RAG. | US-03 |
| CP04 | Solicitar «Explícalo de manera más sencilla». | La nueva respuesta simplifica la explicación contextual. | US-04 |
| CP05 | Reiniciar la conversación. | Desaparecen los mensajes previos de la sesión. | US-05 |
| CP06 | Generar una respuesta. | El indicador de procesamiento es visible durante la espera. | US-06 |
| CP07 | Simular credenciales incorrectas o modelo no autorizado. | Aparece error comprensible sin revelar secretos ni bloquear la aplicación. | US-07 |
| CP08 | Abrir una conversación nueva. | Aparece el mensaje de bienvenida. | US-08 |
| CP09 | Cambiar instrucciones de un perfil. | Se modifica el comportamiento sin editar el cliente Bedrock. | US-09 |
