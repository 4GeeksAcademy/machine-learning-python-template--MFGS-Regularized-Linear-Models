📝 Instrucciones para construir el modelo de regresion lineal
Datos socio demográficos y de recursos de salud a nivel de condado de EE. UU. (2018-2019)
Se han recopilado datos socio demográficos y de recursos de salud por condado en los Estados Unidos y queremos descubrir si existe alguna relación entre los recursos sanitarios y los datos socio demográficos.

Para ello, es necesario que establezcas una variable objetivo (relacionada con la salud) para llevar a cabo el análisis.

Paso 1: Carga del conjunto de datos a tu modelo
El conjunto de datos se puede encontrar en esta carpeta de proyecto bajo el nombre demographic_health_data.csv. Puedes cargarlo en el código directamente desde el siguiente enlace:

https://raw.githubusercontent.com/4GeeksAcademy/regularized-linear-regression-project-tutorial/main/demographic_health_data.csv
O descargarlo y añadirlo a mano en tu repositorio. En este conjunto de datos encontrarás una gran cantidad de variables, que encontrarás definidas aquí.

- FIPS Code for the County: Código de identificación de los condados de los EEUU. Los dos primeros digitos representan el Estado, los últimos tres dígitos identifican el condado dentro de ese estado. 
- TOT_POP: Población total, de las estimaciones de población del censo de 2019 en EEUU.
- Nº 0-9: Población de 0 a 9 años.
- N_POP_CHG_2018 → Cambio numérico en la población residente entre el 1 de julio de 2017 y el 1 de julio de 2018 (población final - población inicial).
- GQ_ESTIMATES_2018 → Estimación de la población en viviendas colectivas (Group Quarters), como prisiones, residencias para ancianos, bases militares, etc., al 1 de julio de 2018.
- R_birth_2018 → Tasa de natalidad en el período del 1 de julio de 2017 al 30 de junio de 2018. Se mide como nacimientos por cada 1,000 habitantes.
- R_death_2018 → Tasa de mortalidad en el mismo período. Representa el número de muertes por cada 1,000 habitantes.
- R_NATURAL_INC_2018 → Tasa de incremento natural, es decir, la diferencia entre la tasa de natalidad y la tasa de mortalidad, en el período 1 de julio de 2016 a 30 de junio de 2017.
- R_INTERNATIONAL_MIG_2018 → Tasa neta de migración internacional, que mide la diferencia entre inmigrantes y emigrantes internacionales, en el período 1 de julio de 2017 a 30 de junio de 2018.
- R_DOMESTIC_MIG_2018 → Tasa neta de migración doméstica, que mide cuántas personas se mudaron dentro de EE.UU. entre condados o estados, en el mismo período.
- R_NET_MIG_2018 → Tasa neta total de migración, que combina la migración internacional y doméstica.

📉 Pobreza
POVALL_2018 → Estimación del número total de personas de todas las edades en situación de pobreza en 2018.
PCTPOVALL_2018 → Porcentaje estimado de la población total en situación de pobreza en 2018.
PCTPOV017_2018 → Porcentaje de niños y adolescentes (0-17 años) en pobreza en 2018.
PCTPOV517_2018 → Estimación del porcentaje de niños de 5 a 17 años en familias en pobreza en 2018.
🔹 Interpretación: Estas variables ayudan a analizar cómo afecta la pobreza a distintos grupos de edad en cada condado.

💰 Ingresos del hogar
MEDHHINC_2018 → Ingreso medio por hogar en el condado en 2018.
CI90LBINC_2018 → Límite inferior del intervalo de confianza del 90% para la estimación del ingreso medio.
CI90UBINC_2018 → Límite superior del intervalo de confianza del 90% para la estimación del ingreso medio.
🔹 Interpretación: Estos datos permiten comparar niveles de ingreso entre condados y analizar la incertidumbre en la estimación.

👷‍♂️ Empleo y desempleo
Civilian_labor_force_2018 → Fuerza laboral civil en promedio anual (personas en edad de trabajar, excluyendo militares y personas fuera de la fuerza laboral).
Employed_2018 → Número total de personas empleadas en promedio anual.
Unemployed_2018 → Número total de personas desempleadas en promedio anual.
Unemployment_rate_2018 → Tasa de desempleo, calculada como (Unemployed / Civilian_labor_force) * 100.
🔹 Interpretación: Estas variables permiten medir la situación del empleo en cada condado.

Pobreza → Cuántas personas están en situación de pobreza y qué porcentaje representan.
Ingresos → Nivel medio de ingresos en los hogares y su intervalo de confianza.
Empleo → Cuántas personas trabajan, cuántas están desempleadas y cuál es la tasa de desempleo.

Estas variables están relacionadas con ingresos, disponibilidad de atención médica y estructura demográfica de los condados en EE.UU. en 2018-2019. Aquí te explico cada una:

💰 Ingresos relativos al estado
Med_HH_Income_Percent_of_State_Total_2018 → Muestra el ingreso medio por hogar en el condado como porcentaje del ingreso medio estatal en 2018.
🔹 Ejemplo: Si este valor es 80%, significa que el ingreso medio del condado es el 80% del ingreso medio estatal.
🏥 Recursos de atención médica
Active Physicians per 100000 Population 2018 (AAMC) → Número de médicos en ejercicio por cada 100,000 habitantes en 2018.
Total Active Patient Care Physicians per 100000 Population 2018 (AAMC) → Número de médicos de atención primaria en ejercicio por cada 100,000 habitantes en 2018.
Active Patient Care Primary Care Physicians per 100000 Population 2018 (AAMC) → Similar al anterior, pero enfocado en médicos de atención primaria.
Active General Surgeons per 100000 Population 2018 (AAMC) → Número de cirujanos generales en ejercicio por cada 100,000 habitantes en 2018.
Active Patient Care General Surgeons per 100000 Population 2018 (AAMC) → Número de cirujanos generales en práctica clínica por cada 100,000 habitantes.
📌 Diferencias clave:

"Active" = Médicos en ejercicio.
"Patient Care" = Médicos que trabajan con pacientes directamente.
🏥 Otras métricas de salud
Total nurse practitioners (2019) → Número total de enfermeras practicantes en 2019.
Total physician assistants (2019) → Número total de asistentes médicos en 2019.
Total Hospitals (2019) → Número total de hospitales en el condado en 2019.
ICU Beds_x → Número total de camas en unidades de cuidados intensivos (UCI) en el condado.
👴 Demografía (Adultos Mayores y Población General)
Population Aged 60+ → Número total de personas de 60 años o más en el condado.
Percent of Population Aged 60+ → Porcentaje de la población del condado que tiene 60 años o más.
county_pop2018_18 and older → Número de personas de 18 años o más en el condado en 2018.
🏛 Identificación del Estado y Condado
STATE_FIPS → Código FIPS del estado (los primeros dos dígitos del código FIPS del condado).
📌 Resumen práctico:

Ingresos → Compara el ingreso medio del condado con el del estado.
Médicos y hospitales → Disponibilidad de médicos, enfermeras y hospitales en la región.
Población mayor y camas UCI → Recursos para atender a adultos mayores y pacientes críticos.
Identificación del estado → Código FIPS para análisis geográficos.

🏥 Prevalencia de enfermedades y confianza estadística
La prevalencia mide cuántas personas tienen una enfermedad en una población determinada.
Las variables "Lower 95% CI" y "Upper 95% CI" indican el intervalo de confianza del 95% para la estimación de la prevalencia, lo que significa el rango dentro del cual se espera que esté el valor real en el 95% de los casos.

📊 Condiciones generales de salud
anycondition_prevalence → Tasa de prevalencia de cualquier condición médica en la población.
anycondition_number → Número estimado de personas con cualquier condición médica.
🏋️ Obesidad
Obesity_prevalence → Tasa de obesidad en la población.
Obesity_number → Número estimado de personas con obesidad.
❤️ Enfermedad cardiaca
Heart disease_prevalence → Tasa de enfermedad cardíaca en la población.
Heart disease_number → Número estimado de personas con enfermedad cardíaca.
🫁 Enfermedad pulmonar obstructiva crónica (EPOC / COPD)
COPD_prevalence → Tasa de EPOC en la población.
COPD_number → Número estimado de personas con EPOC.
🍬 Diabetes
diabetes_prevalence → Tasa de diabetes en la población.
diabetes_number → Número estimado de personas con diabetes.
🩸 Enfermedad renal crónica (CKD)
CKD_prevalence → Tasa de enfermedad renal crónica (CKD) en la población.
CKD_number → Número estimado de personas con CKD.
🏙️ Clasificación Urbana-Rural
Urban_rural_code → Indica si un condado es metropolitano (urbano) o no metropolitano (rural) según el tamaño de su población y su cercanía a áreas urbanas.
🔹 Categorías principales:
📌 Condados metropolitanos (urbanos)
1️⃣ Metro con 1 millón de habitantes o más.
2️⃣ Metro con 250,000 a 1 millón de habitantes.
3️⃣ Metro con menos de 250,000 habitantes.

📌 Condados no metropolitanos (rurales)
4️⃣ Área urbana de 20,000+ habitantes, cerca de una metrópoli.
5️⃣ Área urbana de 20,000+ habitantes, lejos de una metrópoli.
6️⃣ 2,500 - 19,999 habitantes, cerca de una metrópoli.
7️⃣ 2,500 - 19,999 habitantes, lejos de una metrópoli.
8️⃣ Completamente rural (<2,500 habitantes urbanos), cerca de una metrópoli.
9️⃣ Completamente rural (<2,500 habitantes urbanos), lejos de una metrópoli.

🔹 Otros códigos:

88 → Desconocido (Alaska, Hawái o no clasificado).
99 → Desconocido (No clasificado por el USDA).
📌 Resumen práctico:
1️⃣ Salud pública → Tasa y número de personas con obesidad, diabetes, enfermedades cardíacas, EPOC y CKD.
2️⃣ Intervalos de confianza → Margen de error en las estimaciones de salud.
3️⃣ Clasificación urbano-rural → Determina si un condado es urbano o rural según su tamaño y cercanía a ciudades.

Paso 2: Realiza un EDA completo
Este segundo paso es vital para asegurar que nos quedamos con las variables estrictamente necesarias y eliminamos las que no son relevantes o no aportan información. Utiliza el Notebook de ejemplo que trabajamos y adáptalo a este caso de uso.

Asegúrate de dividir convenientemente el conjunto de datos en train y test como hemos visto en lecciones anteriores.

Paso 3: Construye un modelo de regresión
Comienza a resolver el problema implementando un modelo de regresión lineal y analiza los resultados. A continuación, utilizando los mismos datos y los atributos por defecto, construye un modelo Lasso y compara los resultados con la regresión lineal base.

Analiza cómo evoluciona el 
R
2
R 
2
 
 cuando el hiperparámetro del modelo Lasso cambia (puedes por ejemplo empezar a probar desde el valor 0.0 e ir aumentándolo hasta un valor de 20). Dibuja estos valores en un diagrama de líneas.

Paso 4: Optimiza el modelo de regresion anterior
Después de entrenar el modelo Lasso, si los resultados no son satisfactorios, optimízalo empleando alguna de las técnicas vistas anteriormente.

