<H2>INFORME</H2>
<p align="center"><img src="img/Diagrama%20%231.png"/></p>
<H3>1. PLANTEAMIENTO DEL PROBLEMA</H3>
<p align="justify">Raspberry Pi es un ordenador de placa reducida, ordenador de placa única u ordenador de placa simple (SBC) de bajo costo desarrollado en el Reino Unido por la Raspberry Pi Foundation, con el objetivo de estimular la enseñanza de informática en las escuelas.El modelo original se convirtió en más popular de lo que se esperaba, hasta incluso vendiéndose fuera del mercado objetivo para usos como robótica. No incluye periféricos (como teclado y ratón) o carcasa.La fundación da soporte para las descargas de las distribuciones para arquitectura ARM, Raspbian (derivada de Debian), RISC OS 5, Arch Linux ARM (derivado de Arch Linux) y Pidora (derivado de Fedora) y promueve principalmente el aprendizaje del lenguaje de programación Python. Otros lenguajes también soportados son Tiny BASIC, C, Perl y Ruby.La mayoría de Raspberry Pis son hechas en una fábrica de Sony en Pencoed, Wales; algunas son hechas en países asiáticos como China o Japón.</p>

<p align="justify"> </p>

<p align="justify"> </p>

<H3>2. OBJETIVOS</H3>
<b>Objetivos Generales</b>
<p align="justify">- Realizar un video explicando e identificando los temas relevantes a manera de un tutorial sobre el tema asignado.</p>
<p align="justify">- Conocer los beneficios de usar una máquina virtual.</p>
<b>Objetivos Específicos</b>
<p align="justify">- Emplear las herramientas que nos brinda Amazon EC2.</p>
<p align="justify">- Generar una máquina virtual con el servicio Amazon EC2.</p>
<p align="justify">- Identificar la variedad de S.O disponibles para la instalación.</p>
<p align="justify">- Reconocer el nivel de seguridad que posee este servicio.</p>
<H3>3. ESTADO DEL ARTE</H3>
<b>Streaming de medios habilitados en la nube mediante Amazon Web Service (AWS)</b><br>
<p align="justify">Amazon Web Service (AWS) es una colección de servicios de computación remota formando una plataforma de computación en la nube, ofreciendo a través de Amazon.com. Los servicios más conocidos son Amazon EC2 y Amazon S3. En donde el servicio es mucho más rápido, escalable y económico siendo eficaz al generar una gran cantidad de servidores físicos.<br><br> 
La transmisión de medios se realiza en computadoras y no en cualquier tipo de uso común. Por lo tanto, este sistema viene a ser, la clave para llevar la transmisión de medios a cada usuario que usa teléfonos inteligentes sin tener que preocuparse por la necesidad de Hardware.<br><br>
El objetivo principal de este sistema propuesto es la transmisión de archivos multimedia a través del servidor de medios utilizando el servicio de AWS. El servidor de medios utiliza Amazon EC2 para la transmisión, mientras que en el almacenamiento de archivos multimedia es hecho en EBS y Simple Storage Service (S3) el cual mantiene la copia de seguridad de estos archivos. Esta transmisión de datos a través de los web servidores de la nube hacia los que utilizan sistemas móviles en lugar de otros, presenta flexibilidad y rapidez al momento de visualizar.<br><br>
Esta flexibilidad se puede usar para abordar problemas importantes que enfrentan aplicaciones como el tráfico del monitoreo, conciertos en línea, conferencias, etc. Tomando en cuenta que una aplicación contara con varias personas en línea en el mismo instante, además de el Bit Rate que será ocupado en el servidor para que el usuario pueda tener una conexión estable con el medio.<br><br></p>
<b>Explorando la migración a la nube, en vivo, en Amazon EC2</b>
<p align="justify">Los usuarios pueden migrar su máquina virtual de un proveedor de nube pública a otro, debido a un menor costo o falta de servicios que se necesiten. Actualmente no es posible instalar una segunda plataforma de virtualización en la nube pública porque la virtualización anidada y la virtualización asistida por hardware están deshabilitadas de forma predeterminada.<br><br>
Dando como resultado, la migración de máquinas virtuales a diferentes proveedores, mayoritariamente de pago, por los beneficios que les otorgan.<br><br>
Este artículo presenta LivCloud, una solución para vivir la migración a la nube. LivCloud está diseñado en criterios bien establecidos para migrar máquinas virtuales en vivo, con sus debidos protocolos de seguridad y permisos adecuados para tener absoluto control al momento de migrar.<br><br>
En este estudio, se evaluó la implementación del diseño básico de LivCloud en Amazon EC2. Esta instancia tiene de cálculo optimizado y procesadores de alto rendimiento. En particular se exploró tres opciones desarrolladas. Estas opciones están siendo probadas por primera vez en EC2 donde se podrá cambiar el valor que se tiene de control preestablecido a uno con mayores permisos, además cambiar los valores de los registros significativamente ayudara a habilitar la virtualización anidada en Amazon EC2.<br><br>
Es por esto y más, que los usuarios preferirían usar Amazon EC2 como su nube, para poder realizar tantos procesos como ellos los requieran, además facilitándoles la migración de su anterior servidor a este nuevo, de manera segura y rápido.<br><br></p>
<b>Aprovisionamiento y ejecución basados en costos de un servicio informático intensivo en el Amazon EC2</b>
<p align="justify">La decisión de migrar un servicio a un sistema basado en la nube debe tener en cuenta muchos aspectos diferentes. Entre ellos, los costos económicos es uno de los más importantes. Este artículo describe cómo un servicio de esta calidad, basado en un enfoque de administrador de tareas, se ha migrado de una infraestructura de red a la infraestructura Amazon Elastic Compute Cloud (EC2).<br><br> 
También se ha propuesto un modelo basado en costos para su evaluación a instancias económicas del servicio en la nube, donde se tomará en cuenta los costos informáticos, de almacenamiento y despliegue de la plataforma. <br><br>
El modelo incluye una amplia gama de diferentes tipos de instancias y políticas de compra proporcionadas por Amazon EC2, también respecto a costos esta propuesta se integra en el asunto para la implementación y ejecución del servicio, haciendo posible la interacción con los servicios web de Amazon para contratar los recursos en la nube necesarios y utilizarlos de manera eficiente para la ejecución del servicio, con esto el articulo trata de dar a entender los costos vienen a ser económicos referentes a la gran cantidad de beneficios que se obtiene contratando Amazon EC2.<br><br></p>

<H3>4. MARCO TEORICO</H3>
<p align="justify">Amazon Elastic Compute Cloud proporciona capacidad de computación escalable en la nube de AWS (Amazon Web Services)
En el instante de tomar el termino escalable, nos estamos refiriendo a que cada usuario puede contratar lo que desee y configurar su servicio como él quiera, es decir no hay un solo modo de utilizar AWS, sino múltiples.</p>

<p align="justify">El uso de Amazon EC2 tiene una serie de beneficios, uno de ellos y el más importante es aquel que elimina la necesidad de invertir en hardware, de tal manera que se puede desarrollar aplicaciones e implementar aplicaciones con mayor rapidez, evitándonos tener que realizar distintos ensambles para mayor velocidad en nuestra máquina virtual, no menos importante tenemos también la disponibilidad de lanzar tantos servidores a la necesidad del usuario, en los cuales podemos administrar la seguridad, velocidad y almacenamiento.</p>

<p align="justify">Por parte de las herramientas que brinda Amazon EC2, daremos a conocer una de las principales, las cuales toman el nombre de plantillas preconfiguradas para las instancias, las cuales se conocen como imágenes de máquina de Amazon en las cuales se encuentra todo lo necesario para generar nuestra máquina virtual, incluyendo el sistema operativo y software adicional.</p>

<p align="justify">Otra herramienta que nos brinda este increíble servicio, es reconfigurar los tipos de instancias, es decir, configurar el CPU en sí, memoria, almacenamiento, capacidad de red.</p>

<p align="justify">Generar una máquina virtual se ha facilitado mucho más para los desarrolladores, compañías, sin olvidar la rapidez con la cual pueden crearla, teniendo a su paso precios al alcance del bolsillo del usuario, si bien es cierto, la comparación del uso de Amazon EC2 a la inversión en hardware vendría a economizar al usuario en gran cantidad, ya que el mantenimiento correría por parte del servicio, al igual que sus actualizaciones, dando todas las facilidades tanto como de instalación, manejo y pagos módicos al usuario.</p>

<p align="justify">Amazon EC2, tiene un repositorio extenso dentro de su servicio, con variedad de herramientas, S.O., tomados con el nombre de AMI (Amazon Machine Image), para que el servicio cumpla con las necesidades del usuario, además de poseer las licencias de las seguridades necesarias para mantener a salvo nuestra máquina virtual.</p>

<p align="justify">AMI está compuesto por 4 fuentes: publicación de AWS, AMI publicado por un socio en el mercado de AWS con paquetes de software preinstalados, AMI generadas por el cliente a partir de instancias de Amazon EC2 existentes y AMI cargadas desde servidores virtuales.</p>

<p align="justify">Amazon EC2, tiene un repositorio extenso dentro de su servicio, con variedad de herramientas, S.O., para que el servicio cumpla con las necesidades del usuario, además de poseer las licencias de las seguridades necesarias para mantener a salvo nuestra máquina virtual.</p>

<p align="justify">Respecto a la seguridad que se tiene en un Cloud Computing Machine, podemos observar que Amazon EC2 ha podido cubrir casi todos los agujeros o filtros de seguridad en los que podrían haber ocurrido una serie de inconvenientes por parte de terceros. Estos protocolos de seguridad, APIs, tienen que dar efectividad al usuario que su máquina virtual se encuentra segura y también brindarle el acceso al usuario para que él pueda modificar parte de la red, direccionamiento, protocolos, licencias de seguridad dentro de su máquina virtual sin ningún peligro. Por ello el servicio tomo ciertas medidas como que la información de inicio de sesión sea segura para las instancias con pares de claves, es decir, AWS almacena la clave publica y el usuario guarda la clave privada. No obstante Amazon EC2 tiene en cada de las instancias un firewall que permite al usuario especificar los protocolos, los puertos y los rangos de direcciones de IP por medio de grupos de seguridad internos del servicio.</p>

<H3>5. DIAGRAMAS</H3>
<p align="center"><img src="img/Diagrama%20%231.png"/></p>

<H3>6. LISTA DE COMPONENTES</H3>
<p align="center"><img src="img/RecursosTI.png"/></p>

<H3>7. MAPA DE VARIABLES</H3>
<p align="center"><img src="img/AmazonEC2.png"/></p>
<p align="justify">La creación de una cuenta en <b>AWS</b> de tipo <b>ESTUDIANTIL</b> para el uso del servicio <b>AMAZON EC2</b>, viene a ser de tipo visual. Siendo la parte fundamental en la creación de nuestra máquina virtual, ya que sin ella no tendríamos acceso alguno a nuestro portal, y sin ser de tipo estudiantil no tendríamos ciertas funciones disponibles a menos que sea de pago.</p>

<H3>8. EXPLICACION DEL CODIGO FUENTE</H3>
<p align="justify">Nuestro proyecto no posee código fuente.</p>

<H3>9. DESCRIPCION DE PRERREQUISITOS Y CONFIGURACION</H3>
<b>Aplicaciones Secundarias</b>
<p align="justify">-	Control Remoto de Escritorio: Propiamente de la creación de Amazon EC2 para la reproducción visual de nuestra máquina virtual ya que en el sitio web solo poseemos la consola.</p>
<p align="justify">-	Navegador web (Google Chrome, Microsoft Edge): Tanto para la creación de la cuenta de usuario, como para la selección del sistema operativo a instalar.</p>
<b>Configuración del terminal</b>
<p align="justify">-	Se debe tener una cuenta ya sea ESTUDIANTIL o de PAGO para obtener ciertos beneficios a la hora de tener la máquina virtual, tanto en funciones como rapidez en transición de datos.</p>
<p align="justify">-	Ingresar el usuario y contraseña emitidos al correo electrónico para el uso únicamente de la máquina virtual mediante la aplicación secundaria.</p>
<p align="justify">-	Las MAQUINAS BASICAS tienen muy poco almacenamiento tanto en Disco Duro (30GB) como en Memoria RAM (1GB) es por ello que nos servirá únicamente para cosas muy sencillas.</p>
<p align="justify">-	El uso del control remoto de escritorio servirá para poder configurar de manera adecuada nuestra máquina virtual, como si tuviésemos una física.</p>

<H3>10. APORTACIONES</H3>
<b>Máquina Virtual</b>
<p align="justify">Es un software que simula un sistema de computación y puede ejecutar programas como si fuese una computadora real, pero lo hace de manera aislada además emula todos los elementos que posee una máquina en físico entre los componentes que simula se encuentran: disco duro, memoria RAM, tarjetas de red, tarjeta gráfica, etc.</p>
<b>Sistema Operativo</b>
<p align="justify">Es un conjunto de programas especialmente diseñado para hacer de intermediarios entre el usuario y la computadora, estos programas nos sirven para controlar el hardware de manera fácil y conveniente para el usuario, puede decirse que es corazón de la máquina ya que este tiene prioridad de ejecución ante otras aplicaciones además de controlar todos los periféricos disponibles en la computadora, los sistemas operativos más utilizados son: Microsoft Windows, Mac OS X y Linux Ubuntu.</p>
<b>Tipos de Sistemas operativos</b>
<p align="justify">- Sistema monoprocesador:  En el sistema monoprocesador existe una sola unidad de procesamiento central (CPU) capaz de ejecutar una serie de instrucciones de índole general.<br><br>
- Sistemas multiprocesadores: También llamados sistemas paralelos o estrechamente acoplados, los sistemas multiprocesadores tienen dos o más CPU que comparten buses y a veces el reloj, la memoria y los dispositivos periféricos. Los hay de dos tipos:<br>
• Multiprocesador asimétrico: cada procesador tiene una tarea específica.<br>
• Multiprocesadores simétricos: todos los procesadores realizan las mismas tareas.<br><br>
- Sistemas distribuidos: Un sistema distribuido presenta una colección de procesadores que no comparten memoria o reloj, y se comunican por una red interconectada.<br><br>
- Sistemas operativos de equipos portátiles: Los equipos portátiles de mano en este caso se refiere a aquellos dispositivos de pequeñas dimensiones que pueden ser manipulados con una mano, como por ejemplos las tabletas, los teléfonos inteligentes y las notebooks. Adicionalmente, los sistemas operativos de teléfonos deben adicionar componentes para las comunicaciones y la interface.<br><br>
- Sistemas operativos empotrados o en tiempo-real: Son los sistemas operativos instalados en los dispositivos médicos, electrónicos, electrodomésticos, automóviles, entre otros. Se encargan de tareas específicas del equipo en cuestión como:<br>
•	Ahorrar la potencia de la batería.<br>
•	Ajustarse a tiempos limitados.<br>
•	No requiere supervisión humana.<br></p>

<b>Parches de Seguridad</b>
<p align="justify">Es un conjunto de cambios que se aplican a un software para corregir los errores o vulnerabilidades en programas o sistemas operativos, generalmente estos parches de seguridad (actualización de seguridad) son fabricados por fabricantes de software tras la detección de alguna vulnerabilidad y estos se instalan automáticamente o manualmente por el usuario.</p>

<H3>11. CONCLUSIONES</H3>
<p align="justify">-	Se pudo comprender los distintos beneficios que trae generar una máquina virtual ante una física.<br>
-	Dentro de las herramientas que nos brinda este servicio, pudimos hacer uso del Control Remoto del Escritorio, facilitándonos más el uso de nuestra máquina.<br>
-	Se genero con facilidad, rapidez nuestra máquina virtual dentro de Amazon EC2.<br>
-	El repositorio que carece este servicio, es extenso, cumpliendo con todas las expectativas ante los sistemas operativos que se necesiten.<br>
-	Cada uno de los protocolos de seguridad del servicio, satisfacen al usuario, entregando toda la confianza a su servicio.<br></p>

<H3>12. RECOMENDACIONES</H3>
<p align="justify">-	Si la cuenta va a ser de tipo GRATUITA o ESTUDIANTIL, se deberá tener en cuenta que la máquina virtual solamente será para procedimientos extremadamente básicos.<br><br>
-	Para mayor facilidad de uso, configuración, se recomienda descargar el Control Remoto de Escritorio elaborado por AMAZON EC2 para visualizar su máquina virtual, debido a que la página web solamente posee la CONSOLA para poder configurar nuestra Virtual Machine.<br><br>
-	Tener en cuenta al momento de instalar un sistema operativo, no se lo hace mediante descarga o con la conexión de red, estos sistemas operativos ya vienen precargados en cada servicio, es por ello que solamente tomara ciertos minutos que se genere tu máquina virtual.<br><br>
-	Para el uso del Control Remoto de Escritorio y si la maquina desde donde lo ejecutas no tiene habilitado el virtualizado, se deberá activar esta sección ya sea desde la BIOS o desde nuestro PANEL DE CONTROL, caso contrario no nos permitirá que genere imagen nuestra Virtual Machine.<br></p>

<H3>13. CRONOGRAMA</H3>
<p align="center"><img src="img/Cronograma%20de%20gantt.png"/></p>
<p align="justify"></p>

<H3>14. BIBLIOGRAFIA</H3>
<p align="justify">-	Amazon Web Services: Ventajas y Desventajas. (n.d.). Recuperado en Mayo 30, 2020, de https://www.ambit-bst.com/blog/amazon-web-services-ventajas-desventajas.<br><br>
-	AWS | Elastic compute cloud (EC2) de capacidad modificable en la nube. (n.d.). Recuperado en Mayo 30, 2020, de https://aws.amazon.com/es/ec2/.<br><br>
- Cloud enabled media streaming using Amazon Web Services - IEEE Conference Publication. (n.d.). Recuperado en Mayo 30, 2020, de https://ieeexplore.ieee.org/document/8089150.<br><br>
- Cost-driven provisioning and execution of a computing-intensive service on the Amazon EC2 - OUP Journals & Magazine. (n.d.). Recuperado en Mayo 30, 2020, de https://ieeexplore.ieee.org/document/8488886.<br><br>
-	CREAR GRATIS UNA MAQUINA VIRTUAL EN LA NUBE - YouTube. (n.d.). Recuperado en Mayo 30, 2020, de https://www.youtube.com/watch?v=aKLnNBD2A98.<br><br>
- Exploring Live Cloud Migration on Amazon EC2 - IEEE Conference Publication. (n.d.). Recuperado en Mayo 30, 2020, de https://ieeexplore.ieee.org/document/8114505.<br><br>
-	Google cloud vs AWS. Comparativa, pros y contras. (n.d.). Recuperado en Mayo 30, 2020, de https://blog.powerdata.es/el-valor-de-la-gestion-de-datos/google-cloud-vs-aws.-comparativa-pros-y-contras.<br><br>
-	Ventajas y desventajas del Cloud Computing | ENAE. (n.d.). Recuperado en Mayo 30, 2020, de https://www.enae.es/blog/ventajas-y-desventajas-del-cloud-computing#gref.<br><br>
-	¿Qué es Amazon EC2? - Amazon Elastic Compute Cloud. (n.d.). Recuperado en Mayo 30, 2020, de https://docs.aws.amazon.com/es_es/AWSEC2/latest/UserGuide/concepts.html.<br><br>
-	¿Qué es Amazon Elastic Compute Cloud (Amazon EC2)? (n.d.). Recuperado en Mayo 30, 2020, de https://www.josemariagonzalez.es/amazon-web-services-aws/que-es-amazon-elastic-compute-cloud-amazon-ec2.html/.<br><br>
-	¿Qué es y para qué sirve un diagrama de Gantt? (n.d.). Recuperado en Mayo 30, 2020, de https://blog.teamleader.es/diagrama-de-gantt.<br></p>

<H3>15. ANEXOS</H3>
<H3>15.1 MANUAL DE USUARIO</H3>
<H3>15.2 HOJAS TECNICAS</H3>
<p align="justify">Nuestro proyecto no posee hojas técnicas.</p>
