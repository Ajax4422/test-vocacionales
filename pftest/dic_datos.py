ocupacion_dic = {
    1: ('OFICIOS', r' La principal característica que encuadra las actividades desempeñadas por los profesionales '
                    r'pertenecientes a este grupo ocupacional es la habilidad manipulativa como competencia de mayor'
                    r' valor para la ejecucion de estos trabajos, los oficios. En ocasiones ayudados por maquinaria '
                    r'y herramienta específica, la aptitud manipulativa es esencial. Ej.: peluquero/a, vidriero, '
                    r'modista, tapicero, herrero, relojero, joyero, albañil, yesero, etc '),
    2: ('AGROPECUARIA, PESCA Y MINERIA', r' Actividades desempeñadas en el campo, la ganadería, la pesca y '
                                            r'la minería: Agricultura, ganadería, horticultura, floricultura, '
                                            r'minería, picapedrería, pesca, expertos en trabajos de piscifactoría, '
                                            r'agentes forestales, etc.'),
    3: ('TRANSPORTES', r' Profesiones relacionadas con los transportes terrestres, marítimos ó aéreos de '
                        r'viajeros o de mercancías. Ej. Conductor de autobús, camionero, taxista, ferroviario, '
                        r'conductor de metro, capitán de barco mercante, oficial de buque crucero, piloto civil, etc.'),
    4: ('CUERPOS DE SEGURIDAD Y SERVICIOS DE PROTECCION', r' Profesiones cuya funciones primordiales consisten en la '
                                                            r'defensa del territorio, el mantenimiento del orden '
                                                            r'público, la prevención y la investigación de conductas '
                                                            r'delictivas y la protección a las personas o a los '
                                                            r'bienes. Ej., oficial ó suboficial de las fuerzas '
                                                            r'armadas, policía local, guardia civil, mozo de escuadra, '
                                                            r'guarda jurado, guardaespaldas, vigilante, etc.'),
    5: ('SOPORTE ADMINISTRATIVO. TRABAJO DE OFICINA', r' Está compuesto por profesiones cuyo desempeño principal es la '
                                                        r'gestión administrativa: escritura, lectura, transcripción, '
                                                        r'selección, elaboración y archivo de documentación relacionados '
                                                        r'con una entidad, grupo, organización o empresa, puede implicar '
                                                        r'o no la atención directa al público. Empleado de banca, '
                                                        r'gestor//a administrativo//a, secretario//a, telefonista, '
                                                        r'oficial de correos, recepcionista, etc.'),
    6: ('COMERCIAL', r' Se incluyen profesiones relacionadas con el mundo del comercio, las ventas, los negocios y la '
                        r'vida empresarial. Ej., economista, comerciante, vendedor, agente de cambio y bolsa, '
                        r'asesor de inversiones, agente de seguros, dirección y administración de empresas, marketing, '
                        r'relaciones públicas, servicios al consumidor (peluquería, hostelería, turismo), etc.'),
    7: ('SERVICIOS SOCIALES ', r' Este grupo está integrado por profesiones que reportan un servicio para la población '
                                r'en general y por el desarrollo de la sociedad en igualdad, justicia, para que la '
                                r'comunidad adquiera los derechos mínimos constitucionales y la evolución hacia la '
                                r'Sociedad de Valores sea efectiva, proporcionando ayuda y bienestar a los colectivos '
                                r'con mayor demanda y necesidades de carácter urgente: atención a colectivos en riesgo, '
                                r'análisis de problemáticas como la marginación, atención y asesoramiento a familias '
                                r'con graves situaciones socioeconómicas, integración de discapacitados. Requiere '
                                r'aptitudes de empatía, habilidades sociales, y una clara '
                                r'orientación/preocupación/conciencia social: Geriatría, trabajo social, '
                                r'educación social, religiosos'),
    8: ('EDUCACIÓN Y CULTURA', r' Implican trabajos relacionados con la formación y educación, cultura y difusión de la'
                                r' información. Ej.: profesor de primaria o secundaria, profesor de educación '
                                r'especial, orientador, pedagogo, monitor de tiempo libre, bibliotecario, '
                                r'traducción e interpretación, gestión de museos.'),
    9: ('HUMANIDADES Y CIENCIAS SOCIALES', r' Areas profesionales relacionadas con el estudio de las Ciencias Humanas y'
                                            r' las Ciencias Sociales, como sociología, abogacía, filosofía, psicología, '
                                            r'filología, historia, periodismo, redacción de noticias en radio, TV, '
                                            r'etc. '),
    10: ('CIENCIAS DE LA SALUD', r' Profesiones relacionadas con la prevención, el diagnóstico y el tratamiento de la '
                                    r'salud. Ej., medicina, enfermería, farmacia, veterinaria, auxiliar de clínica, '
                                    r'fisioterapia, terapia ocupacional, óptica y optometría, prótesis dental, etc. '),
    11: ('CIENCIAS DE LA NATURALEZA Y MATEMATICAS', r' Profesiones relacionadas con las Ciencias experimentales o '
                                                    r'físico-naturales y las Matemáticas. Ej. Profesionales '
                                                    r'especialistas en Biología, Física, Química, Geología, '
                                                    r'Ciencias del Mar, Matemáticas, Estadística, etc.'),
    12: ('TECNICA Y TECNOLOGIA', r' Agrupa las profesiones relacionadas con la Mecánica, la Técnica, las Tecnologías '
                                    r'de la Información y la Comunicación (Informática, Comunicaciones, telemática, '
                                    r'como analista de sistemas, analista de aplicaciones científicas, programador, '
                                    r'experto en redes de comunicación e Internet, etc), Ingenierías (Industrial '
                                    r'agrónomos, forestal, materiales, electrónica, telecomunicaciones, caminos, '
                                    r'etc); otras profesiones en este grupo son las vinculadas a la arquitectura, '
                                    r'así como los técnicos especialistas en artes gráficas, automoción, electricidad, '
                                    r'electrónica, técnico de sonido, gemología, etc.'),
    13: ('ARTES', r' Se incluyen aquí las profesiones relacionadas con las siete artes clásicas: Literatura, Pintura, '
                    r'Escultura, Arquitectura, Música, Danza y Cine, además de las artes aplicadas y arte dramático. '
                    r'Ej. músico, novelista, escultor, decorador, restaurador de obras de arte, guionista de cine, '
                    r'actor, diseñador/a de moda, arquitecto, bailarín/a etc.'),
    14: ('EDUCACION FISICA Y DEPORTES', r' Deportista profesional, profesor de educación física, entrenador deportivo, '
                                        r'monitor de esquí, profesor de educación física, etc.')
}

materia_dic = {
    1: (r'Matemáticas', r'Algebra, Geometría, Cálculo, Estadística, Matemática aplicada a la Economía, etc.'),
    2: (r'Ciencias', r'Física, Química, Ciencias Naturales, Biología, Geología, Ciencias de la Tierra y del Medio '
                     r'Ambiente, etc.'),
    3: (r'Lenguaje', r'Lengua castellana, Literatura, Comentarios de Textos, Composición Escrita, etc.'),
    4: (r'Idiomas', r'Inglés, Francés, Alemán, Italiano, Latín, Griego, etc.'),
    5: (r'Ciencias Sociales', r'Filosofía, Historia, Geografía, Sociología, Psicología, Educación Cívica, etc.'),
    6: (r'Arte', r'Historia del Arte, Dibujo artístico, Pintura, Escultura, Diseño, Cerámica, Esmalte, Volumen, '
                 r'Técnicas de expresión gráfico-plástica, etc.'),
    7: (r'Música', r'Solfeo, Canto, Composición, Interpretación Instrumental, etc.'),
    8: (r'Teatro', r'Expresión oral, Expresión corporal, Interpretación, Dirección teatral o de cine, Escenografía, '
                   r'etc.'),
    9: (r'Imagen y Sonido', r'Fotografía, Cine, Video, etc.'),
    10: (r'Oficina', r'Contabilidad: Mecanografía, Técnicas de Oficina'),
    11: (r'Administración de Empresas', r'Ventas, Relaciones laborales, Derecho Mercantil y Fiscal, Gestión de '
                                        r'personal, Legislación laboral, etc.'),
    12: (r'Trabajos de Taller', r'Marquetería, Imprenta, Encuadernación, Macramé, Carpintería, Torno, Mecánica de '
                                r'motores, etc.'),
    13: (r'Tecnología', r'Dibujo Técnico, Interpretación de planos, Experimentos de Laboratorio, Electrónica, '
                        r'Tecnología, industrial, Electrotecnia, etc.'),
    14: (r'Educación Física y Deportes', r'Gimnasia, Atletismo, Baloncesto, Natación, etc.'),
    15: (r'Higiene y Seguridad', r'Dietética, Prevención de accidentes, Prevención de SIDA, Prevención del consumo '
                                 r'de drogas, primeras curas, etc.'),
    16: (r'Informática', r'Manejo de ordenadores, Lenguajes y programación, Diseño de páginas web, mantenimiento y '
                         r'reparación de equipos, gestión de redes, etc.')
}

habilidad_dic = {
    1: (r'Artística', r'Aptitud para el dibujo, pintura, decoración, escultura, diseño, etc. Percepción estética y '
                      r'apreciación de la belleza. Creatividad, imaginación.'),
    2: (r'Numérica', r'Rapidez y precisión trabajando con números, haciendo operaciones aritméticas, recopilando '
                     r'datos o medidas, analizando estadísticas, etc.'),
    3: (r'Liderazgo', r'Aptitud para la dirección de actividades en grupo, saber tomar decisiones, ser solicitado por '
                      r'otros para llevar a cabo una acción o ejecutar una idea o proyecto, etc.'),
    4: (r'Musical', r'Saber tocar un instrumento, cantar en una coral, componer música, etc.'),
    5: (r'Físico-deportiva', r'Habilidad en la coordinación del cuerpo en movimiento, resistencia, muscular, fuerza, '
                             r'flexibilidad. agilidad, etc.'),
    6: (r'Manual', r'Saber trabajar con las manos, tanto en trabajos de esfuerzo físico como en actividades de '
                   r'precisión.'),
    7: (r'Lingüística', r'Dominio de la expresión verbal, tanto oral como escrita. Uso correcto del idioma.'),
    8: (r'Didáctica', r'Saber ayudar a los demás a aprender, saber enseñar.'),
    9: (r'Concentración', r'Habilidad para mantener la atención en una tarea de manera constante o durante bastante '
                          r'tiempo. Atención a los detalles. Resistencia a la monotonía.'),
    10: (r'Mecánica', r'Aptitud para el trabajo con máquinas o herramientas. Saber reparar aparatos, facilidad para '
                      r'la comprensión del funcionamiento de mecanismos y sistemas de procesos mecánicos.'),
    11: (r'Persuasión', r'Capacidad de influir en las demás personas. Saber convencer. Saber vender un producto o '
                        r'servicio, la presentación de una idea de manera convincente, fluidez verbal, habilidades '
                        r'comunicativas, dominio del lenguaje. Negociación.'),
    12: (
        r'Matemática',
        r'Resolución de problemas matemáticos, comprensión de relaciones numéricas y lógica matemática.'),
    13: (r'Científica', r'Curiosidad y capacidad para la compresión de los principios científicos; disposición hacia '
                        r'la observación y experimentación científica; afán de encontrar explicación a los hechos, '
                        r'situaciones o sucesos; etc.'),
    14: (r'Espacial', r'Facilidad para la representación mental de figuras u objetos de dos o tres dimensiones, '
                      r'la diferenciación clara de formas y volúmenes, el posicionamiento en el espacio.'),
    15: (r'Social', r'Aptitudes para trabajar con las personas, empatía, don de gentes, amabilidad, respeto, '
                    r'capacidad de afrontamiento de situaciones conflictivas, estrés, tensión. Prevenir y resolver '
                    r'conflictos.'),
    16: (r'Administrativa', r'Habilidades para la mecanografía, utilización de calculadoras, procesadores de textos. '
                            r'Habilidad en tareas de oficina en general. Orden y sistematicidad.')
}

valor_dic = {
    1: (r'Disponibilidad de tiempo', r'Tener una ocupación que permita flexibilidad horaria, para poder compaginarlo '
                                     r'con la realización de otras actividades.'),
    2: (r'Independencia', r'Poder cumplir las tareas ocupacionales de manera autónoma, posibilitando la consecución '
                          r'de ideas propias, convicciones, procesos propios de trabajo, desarrollando nuestra propia '
                          r'perspectiva o protocolos de actuación para alcanzar los objetivos o resultados '
                          r'demandados.'),
    3: (r'Alcanzar Prestigio', r'Adquirir reconocimiento, reputación, popularidad por los éxitos conseguidos en el '
                               r'trabajo. Destacar entre las personas que ejercen la misma profesión.'),
    4: (r'Altruismo', r'Poder ayudar a los demás y facilitar su bienestar. Solidaridad con los problemas y las '
                      r'dificultades sociales.'),
    5: (r'Trabajo guiado o supervisado:', r'Actuar bajo la dirección o las órdenes de los demás, sin que sea '
                                          r'necesario tener que asumir responsabilidades.'),
    6: (r'Creatividad', r'Tener una ocupación donde se puedan idear cosas, con implicación de la imaginación. '
                        r'Desarrollar pensamientos, realizar propuestas y plantear posibilidades fruto de nuestra '
                        r'capacidad de crear a través de un proceso imaginativo.'),
    7: (r'Relación Social', r'Trabajar en contacto directo con personas. Comunicación, intercambios sociales. Tener '
                            r'la posibilidad de conocer gente, profundizar en las relacioens sociales.'),
    8: (r'Asumir poder y responsabilidad', r'Ser el dirigente o el jefe del grupo en el trabajo, tener capacidad para '
                                           r'tomar decisiones, ser el líder que guía y es responsable de la actuación '
                                           r'de otras personas. Coordinar, supervisar, motivar, dirigir, y asesorar.'),
    9: (r'Seguridad en la ocupación', r'Tener un trabajo fijo o estable, donde la probabilidad de quedar '
                                      r'desocupado/desempleado sea mínima, que la ocupación garantice el trabajo (y '
                                      r'por ende la remuneración que este lleva asociada) de por vida. La percepción '
                                      r'de estabilidad y seguridad laboral como primacía.'),
    10: (r'Remuneración', r'Recibir un buen sueldo por el trabajo desarrollado.'),
    11: (r'Actividad rutinaria', r'Realización de un trabajo con escasa complejidad, muy organizado en un sistema '
                                 r'cerrado, donde el desarrollo de la actividad diaria es muy similar día a día, '
                                 r'no está sujeto a demasiados cambios y con facilidad se adquiere destreza en la '
                                 r'ejecución de las tareas implicadas, que por lo general serán de carácter '
                                 r'repetitivo y mucha similitud entre ellas.'),
    12: (r'Variedad-Diversidad', r'Tener la oportunidad de realizar una diversidad de trabajos, viajar, emprender '
                                 r'nuevas tareas, que puedan implicar cierta aventura, sistemas de trabajo abiertos, '
                                 r'donde no se conoce siempre el desarrollo, y se pueden alcanzar los resultados a '
                                 r'través de distintos itinerarios.')
}

intereses = {
    1: (r'Cuando realizo algún trabajo o tarea me gusta hacerlo de manera original, de forma diferente a la mayoría '
        r'de personas.', 'A'),
    2: (r'Soy una persona siempre dispuesta a cooperar con los demás y participar en actividades sociales.', 'S'),
    3: (r'Soy capaz de explicar las cosas con claridad y entusiasmo, consiguiendo convencer y persuadir de mis puntos '
        r'de vista', 'E'),
    4: (r'Me gusta aceptar las sugerencias que se me hacen y cumplir con responsabilidad las instrucciones recibidas '
        r'de mis superiores.', 'O'),
    5: (r'Concidero que soy una persona práctica, me gusta ocuparme en trabajos útiles en los que pueda ver resultados '
        r'rapidos.', 'R'),
    6: (r'Me divierten los juegos que requieren pensamiento analítico: Ajedrez, cuestionarios matemáticos, deducir '
        r'combinaciones, aplicar estrategias, etc.', 'C'),
    7: (r'Me gusta manipular herramientas o máquinas y ser capaz de aprovechar todo su potencial.', 'R'),
    8: (r'Se controlar mis emociones y sentimientos, pienso antes de actuar y analizo las consecuencias de mis actos.',
        'C'),
    9: (r'Me siento una persona independiente, actuó sin hacer caso a las costumbres o normas establecidas por la '
        r'sociedad', 'A'),
    10: (r'Me considero una persona empática, capaz de comprender a las demás y de despertar en ellas optimismo', 'S'),
    11: (
        r'Normalmente me considero el líder del grupo donde me encuentro y que los demás reconozcan mis cualidades',
        'E'),
    12: (r'Procuro tener mis cosas bien ordenadas y realizo mi trabajo con pulcritud', 'O'),
    13: (r'Prefiero dedicarme a trabajos de tipo manual que otras ocupaciones que se basan en uso de ideas y/o '
         r'palabras', 'R'),
    14: (r'Cuando inicio el estudio de un tema nuevo me entusiasma profundizar y no lo dejo hasta comprender e '
         r'interpretar todo', 'C'),
    15: (r'Me gusta dedicarme a trabajos que se puedan hacer con toda libertad, sin condiciones e imposiciones', 'A'),
    16: (r'Una de mis características es ser una persona generosa y servicial para prestar ayuda a los demás para '
         r'que resuelvan sus problemas o dificultades', 'S'),
    17: (r'A menudo consigo que los demás se den cuenta de las cosas positivas y agradables de las situaciones '
         r'o acontecimientos', 'E'),
    18: (r'Creo que soy eficaz y tengo sentido práctico en las tareas de organización, estoy atento y me preocupo de '
         r'los detalles', 'O'),
    19: (r'Me atraen las actividades que impliquen el esfuerzo físico', 'R'),
    20: (r'Dedico mucho tiempo a la lectura de libros y artículos científicos', 'C'),
    21: (r'Me considero una persona imaginativa, con inspiración, capaz de dar soluciones nuevas a los '
         r'problemas que se presentan', 'A'),
    22: (r'Me gusta meditar sobre la realidad social y preocupa las injusticias que a veces les suceden a '
         r'algunas personas', 'S'),
    23: (r'Me considero una persona ambiciosa, ansió a llegar a altos puestos de responsabilidad, ser un '
         r'personaje importante', 'E'),
    24: (r'A menudo planifico lo que tengo que hacer de manera realista, metódica y detallada. Me gusta prever las '
         r'cosas y no actuar al azar o improvisado', 'O'),
    25: (r'Prefiero las actividades que tengan relación con manipular objetos o maquinarias', 'R'),
    26: (r'Me siento mejor haciendo las cosas solo, siento que puedo concentrarme mejor en lo que hago', 'C'),
    27: (r'No me gusta la falta de estética en la publicidad grafica', 'A'),
    28: (r'Tengo facilidad de iniciar una conversación con las personas que acabo de conocer y me intereso en '
         r'sus preferencias o aficiones', 'S'),
    29: (r'Pienso que la economía es uno de los factores más importantes para el desarrollo del individuo y '
        r'de la sociedad', 'E'),
    30: (r'Prefiero un mismo tipo de ritmo de trabajo sobre el cambio constante', 'O')
}


tiposO_dic = {
    "R": ("Realista",
          'Son personas que demuestran interés por actividades prácticas, mecánicas, que a menudo exigen esfuerzo '
          'físico; o bien, actividades que comportan el contacto con la naturaleza (cultivar campos, criar animales, '
          'etc). Prefieren trabajar con herramientas y objetos en lugar de trabajar con palabras y personas. Desean '
          'construir cosas y ver resultados prácticos en su trabajo. Normalmente no buscan el contacto social y '
          'evitan hacerse notar. Entre las ocupaciones típicas de esta categoría encontramos: agricultura, mecánica, '
          'carpintería, conducción de vehículos, instalaciones (electricidad, agua, gas), reparaciones (aparatos, '
          'máquinas, etc).'),
    "C": ("Científico",
          "Les gusta observar y experimentar para comprender los fenómenos que les rodean y reflexionar para "
          "comprender procesos lógicos. Resuelven los problemas con el uso de ideas y del lenguaje. Valoran altamente "
          "las matemáticas y el trabajo científico (teoría, investigación el laboratorio, etc). Tienden a ser "
          "personas curiosas, reflexivas, analíticas, teóricas, críticas, estudiosas y metódicas y a menudo les gusta "
          "trabajar solas. Sienten atracción por profesiones relacionadas con la Biología, la Química, "
          "la Arquitectura, la Medicina, la Ingeniería Informática, las Ciencias Sociales, y en general, "
          "la investigación referida a cualquier campo del saber."),
    "A": ("Artístico",
          "Se relacionan con el entorno físico y social utilizando sus sentimientos y su intuición e imaginación. "
          "Demuestran interés por actividades creativas. Frecuentemente prefieren un estilo de vida no convencional, "
          "valoran mucho la independencia y buscan activamente oportunidades de autoexpresión. Tienden a ser "
          "introspectivos. Les suele faltar habilidades de tipo administrativo. Les gusta el contacto con los demás. "
          "Entre las ocupaciones corrientes de estas personas están las referidas a los diferentes tipos de Artes: "
          "escritor, decorador, pintor, diseñador, músico, actor o actriz, etc."),
    "S": ("Social",
          "Son personas que se preocupan del bienestar de los demás y muestran el deseo de ayudarlos. Generalmente se "
          "relacionan bien con todo tipo de personas, tiene buena habilidad de comunicación interpersonal. Son "
          "comprensivos, generosos y sensibles a los problemas de los demás. Buscan oportunidades de expresar su "
          "interés social a través de ocupaciones como las de trabajo social, enfermería, geriatría, educación, etc."),
    "E": ("Emprendedor",
          "Se enfrentan con el mundo mediante una actitud audaz, dominante, enérgica y “agresiva”. Son dinámicos, "
          "organizadores, seguros de ellos mismos. Sienten atracción pro actividades que les proporcionen la "
          "oportunidad de guiar a los demás, persuadirlos e influir en su manera de pensar, o bien, convencerlos para "
          "que se compren sus “productos”. Valoran el dinero, el poder, la posición social. Ocupaciones típicas: "
          "ejecutivos, cargos públicos, empresarios, vendedores, etc."),
    "O": ("Oficina",
          "Adoptan pautas de conducta y normas sancionadas por las costumbres establecidas por la sociedad. Prefieren "
          "ocupaciones con deberes claramente definidos: tareas de carácter rutinario, actividades verbales o "
          "numéricas propias del trabajo de oficina. Son personas ordenadas, sistemáticas, perseverantes y "
          "conformista. Los campos ocupacionales más apropiados a este tipo de personalidad son los de secretaría, "
          "administración, contabilidad, archivos, telefonía, cartería, distribución interna de mensajes, etc.")
}

cor_dic = {
    # Predominante Realista
    "RC": {1: 1, 2: 2, 3: 12, 4: 11},
    "RA": {1: 2, 2: 13, 3: 1, 4: 14},
    "RS": {1: 1, 2: 7, 3: 4},
    "RE": {1: 1, 2: 2, 3: 6, 4: 3},
    "RO": {1: 1, 2: 5, 3: 3, 4: 14},
    # Predominante Cientifico
    "CR": {1: 12, 2: 11, 3: 1, 4: 2},
    "CA": {1: 11, 2: 12, 3: 13, 4: 10},
    "CS": {1: 10, 2: 11, 3: 9, 4: 8},
    "CE": {1: 12, 2: 6, 3: 9},
    "CO": {1: 11, 2: 12, 3: 5, 4: 9},
    # Predominante Artistico
    "AR": {1: 13, 2: 2, 3: 1, 4: 14},
    "AC": {1: 13, 2: 12, 3: 11, 4: 9},
    "AS": {1: 13, 2: 8, 3: 9, 4: 7},
    "AE": {1: 13, 2: 6, 3: 7, 4: 9},
    "AO": {1: 13, 2: 5, 3: 8},
    # Predominante Social
    "SR": {1: 7, 2: 1, 3: 9},
    "SC": {1: 7, 2: 10, 3: 11, 4: 8},
    "SA": {1: 7, 2: 8, 3: 13, 4: 9},
    "SE": {1: 7, 2: 6, 3: 9, 4: 4},
    "SO": {1: 7, 2: 5, 3: 4, 4: 9},
    # Predominante Emprendedor
    "ER": {1: 6, 2: 3, 3: 2, 4: 1},
    "EC": {1: 6, 2: 12, 3: 11},
    "EA": {1: 6, 2: 13, 3: 8, 4: 7},
    "ES": {1: 6, 2: 9, 3: 7, 4: 8},
    "EO": {1: 6, 2: 4, 3: 7, 4: 8},
    # Predominante Oficina
    "OR": {1: 5, 2: 1, 3: 4, 4: 3},
    "OC": {1: 5, 2: 11, 3: 12, 4: 6},
    "OA": {1: 5, 2: 13, 3: 9},
    "OS": {1: 5, 2: 7, 3: 9, 4: 4},
    "OE": {1: 5, 2: 6, 3: 7, 5: 8}
}

tr_dic = {
    #   Materia:            Habilidad           Valores
    1:  ((12, 13, 11, 6), (6, 10, 9, 14), (5, 11, 1, 7)),
    2:  ((12, 11, 14, 16), (6, 5, 10, 2), (11, 9, 2, 1)),
    3:  ((12, 14, 11, 13), (10, 14, 9, 6), (12, 1, 9, 7)),
    4:  ((14, 15, 12, 10), (11, 5, 10, 16), (4, 5, 9, 7)),
    5:  ((10, 3, 16, 4), (16, 2, 7, 9), (5, 11, 7, 9)),
    6:  ((11, 10, 16, 4),   (3, 16, 11, 2),     (8, 7, 3, 10)),
    7:  ((10, 11, 15, 5),   (11, 15, 16, 6),    (4, 7, 9, 12)),
    8:  ((3, 4, 2, 6),      (8, 7, 15, 3),      (4, 6, 7, 8)),
    9:  ((5, 3, 6, 4),      (7, 15, 8, 1),      (2, 6, 7, 8)),
    10: ((2, 1, 15, 16),    (13, 15, 11, 6),    (4, 3, 9, 10)),
    11: ((1, 2, 16, 13),    (13, 12, 14, 8),    (2, 6, 12, 3)),
    12: ((1, 2, 13, 16),    (13, 12, 14, 10),   (6, 12, 3, 10)),
    13: ((6, 7, 8, 9),      (1, 10, 7, 6),      (6, 2, 12, 3)),
    14: ((14, 15, 2, 12),   (5, 6, 8, 14),      (3, 7, 12, 1))
}

def ocupaciones_lista():
    lista_ocupaciones =[]
    for key, value in ocupacion_dic.items():
        lista_ocupaciones.append({'number': key, 'name': value[0], 'description': value[1]})
    return lista_ocupaciones

def materias_lista():
    lista_materias = []
    for key, value in materia_dic.items():
        lista_materias.append({'number': key, 'name': value[0], 'description': value[1]})
    return lista_materias

def habilidades_lista():
    lista_habilidades = []
    for key, value in habilidad_dic.items():
        lista_habilidades.append({'number': key, 'name': value[0], 'description': value[1]})
    return lista_habilidades

def valores_lista():
    lista_valores = []
    for key, value in valor_dic.items():
        lista_valores.append({'number': key, 'name': value[0], 'description': value[1]})
    return lista_valores