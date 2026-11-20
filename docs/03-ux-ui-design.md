# Diseño UX/UI — AWS AI Practitioner Assistant  

**Artefacto de diseño:** [Archivo Figma — AWS AI Practitioner Assistant](https://www.figma.com/design/tWNL7UNewdMUwDjCH0926V)

## 1. Objetivo del diseño

Definir una interfaz conversacional clara, accesible y de baja complejidad, orientada a estudiantes con conocimientos diversos de AWS e inteligencia artificial. 

## 2. Principios de experiencia de usuario

- **Simplicidad:** la conversación constituye la función central; no se añaden pantallas ni controles innecesarios.
- **Claridad:** el perfil autor de cada respuesta son identificables.
- **Continuidad:** cambiar de perfil conserva los mensajes existentes y el contexto conversacional.
- **Personalización sin etiquetas:** no se solicita al estudiante autodefinirse como principiante o intermedio; puede pedir explicaciones más claras o avanzadas durante el diálogo.
- **Legibilidad:** mensajes del estudiante a la derecha, respuestas de IA a la izquierda, con ancho de lectura limitado y texto ajustado a varias líneas.
- **Retroalimentación:** se prevén estados de carga y errores comprensibles.
- **Accesibilidad y consistencia:** etiquetas explícitas, contraste adecuado, orden lógico y componentes familiares.
- **Factibilidad:** utilizar principalmente componentes nativos de Streamlit.

## 3. Flujo principal del estudiante

1. Abre la aplicación y encuentra el estado de bienvenida, una descripción breve y preguntas sugeridas.
2. Usa el perfil predeterminado **Profesor de IA** o selecciona **Arquitecto AWS** o **Entrenador de certificación** desde la barra lateral.
3. Escribe y envía una pregunta.
4. Observa un estado de procesamiento y posteriormente la respuesta identificada con el perfil que la generó.
5. Continúa preguntando, solicita aclaraciones o profundización y recibe respuestas que toman en cuenta el historial disponible.
6. Puede cambiar de experto desde el selector sin iniciar otro chat; se conserva el historial y las respuestas futuras adoptan las instrucciones del perfil nuevo.

### Estados previstos

- **Bienvenida / chat vacío:** identidad del producto, explicación breve, perfil predeterminado y preguntas de ejemplo.
- **Conversación activa:** mensajes en orden cronológico con alineación distinta según el emisor.
- **Cambio de perfil:** selector actualizado, anotación discreta del cambio y mensajes previos visibles.
- **Procesamiento:** indicador de carga mientras responde el modelo.
- **Error:** aviso legible, sin eliminar innecesariamente el contexto existente.

Los tres primeros estados están representados en los frames de Figma.

## 4. Distribución y wireframe


```text
┌──────────────────────────┬───────────────────────────────────────────────────────┐
│ AI Learning              │ Aprende RAG y LLMs con IA                            │
│ AWS AI Practitioner      │ Conversación · Perfil activo: Arquitecto AWS         │
│                          │                                                       │
│ PERFIL DE EXPERTO        │                           ┌────────────────────────┐  │
│ [Arquitecto AWS      ▾]  │                           │ Tú                     │  │
│                          │                           │ ¿Qué es RAG?           │  │
│ Puedes cambiar de experto│                           └────────────────────────┘  │
│ Se conserva el historial │  ┌─────────────────────────────────┐                 │
│                          │  │ Profesor de IA                  │                 │
│ Temas: RAG y LLMs        │  │ Respuesta con varias líneas     │                 │
│                          │  │ dentro de la burbuja.           │                 │
│                          │  └─────────────────────────────────┘                 │
│                          │  [Perfil cambiado · historial conservado]           │
│                          │                           ┌────────────────────────┐  │
│                          │                           │ Tú: ¿Y en AWS?         │  │
│                          │                           └────────────────────────┘  │
│                          │  ┌─────────────────────────────────┐                 │
│                          │  │ Arquitecto AWS                  │                 │
│                          │  │ Respuesta con salto de línea.   │                 │
│                          │  └─────────────────────────────────┘                 │
│                          │                                                       │
│                          │  [Escribe tu pregunta...]                            │
└──────────────────────────┴───────────────────────────────────────────────────────┘
```

### Comportamiento de mensajes

- Mensajes del estudiante: **derecha**, burbuja gris suave.
- Mensajes de IA: **izquierda**, burbuja azul muy suave.
- Ancho de burbuja del prototipo: **520 px**, con texto interno de hasta **480 px** y salto de línea automático.
- Altura de la burbuja: variable según la longitud del mensaje.
- Cada respuesta muestra el perfil autor, incluso si el perfil activo cambia después.
- El orden de la conversación es cronológico.

## 5. Componentes previstos y equivalencia con Streamlit

| Elemento de diseño | Implementación prevista | Comportamiento |
|---|---|---|
| Cabecera, descripción y notas | `st.title`, `st.caption`, `st.markdown` | Identidad y contexto |
| Barra lateral | `st.sidebar` | Controles persistentes en la vista |
| Selector de experto | `st.selectbox` | Tres perfiles predefinidos |
| Mensajes | `st.chat_message` | Roles, autores y orden cronológico |
| Campo de preguntas | `st.chat_input` | Envío de texto |
| Indicador de procesamiento | `st.spinner` o estado nativo equivalente | Retroalimentación durante la generación |
| Error de conexión o servicio | `st.error` | Explicación comprensible |
| Estado de conversación | `st.session_state` | Historial de una única conversación activa |

## 7. Estilo visual

- **Enfoque:** interfaz académica, minimalista y centrada en la lectura.
- **Tema:** fondo claro, superficies neutras y acentos azules discretos.
- **Jerarquía:** título principal, subtítulo contextual, controles en sidebar y contenido de chat.
- **Tipografía:** sans serif legible, tamaños diferenciados para títulos, etiquetas y contenido.
- **Espaciado:** separación consistente entre bloques, mensajes y controles.

## 8. Frames en Figma

Archivo: https://www.figma.com/design/tWNL7UNewdMUwDjCH0926V

