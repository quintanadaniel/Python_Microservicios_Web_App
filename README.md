Pasos para realizar el proyecto de Microservicios


1. Creamos el docker para la imagen de python 3.8 o mayor, y damos las configuraciones basicas el proyecto 
2. Creamos la imagen del docker compose para levantar nuestra primer contenedor de imagen django y MySQL co el comandos
    "docker-compose up" o usar "up -d" para levantar en background
    "docker-compose stop" => detenemos el docker-compose
    "docker-compose restart" => reiniciamos
    "docker-compose -f $nombre_file $parametro
3. Configuramos en el archovo admin/settings los datos para levantar la base de datos MySql y INSTALLED_APPS y MIDDLEWARE
4. Levantamos el docker-compose para ejecutar una nueva app con el comando 
    "python manage.py startapp products"
5. dede la ruta products/models.py creamos los modelos para nuestra aplicacion.
6. Despues de crear el modelo, entramos en el docker-compose y ejecutamos los comandos para migrar a la BD:
    "python manage.py akemigrations" 
    "python manage.py migrate"
7.
8.
9.
10. Despues de configurar la QUEUE con Rabbit MQ, procedemos a ejecutar los docker-compose con el build, los pasos son los siguientes:
    "docker-compose up --build"
    Si este comando da error por temas de permisos, modificarlos a cada carpeta que este dentro del proyecto, asi sean carpetas ocultas, si aun sigue dando un error por temas de credenciales del docker compose, ejecutar los siguientes comando para actualizar la version
	
	-Actualizamos a la ultima version del docker-compose
		sudo curl -L https://github.com/docker/compose/releases/download/1.26.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
	-Define permissions carpetas ocultas y no ocultas:
		sudo chmod +x /usr/local/bin/docker-compose
		sudo chown --recursive quintanada:quintanada .dbdata
		sudo chown --recursive quintanada:quintanada .dbdata/*
	-Check installed version:
		docker-compose --version 
	Deberia salir por pantalla lo siguiente:
		docker-compose version 1.26.2, build eefe0d31 => el build sin los pasos anteriores saldria como unknow
11. Si hay error para buildear el docker-compose, tener en cuenta de cambiar el usuario y grupo de las carpetas ocultas con el siguiente comando:
	sudo chown --recursive $usuario:grupo $carpeta
12. Tener en cuenta que cuando configuramos los consumer, al habilitar el channel con PIKA, para que no este actualizando el consumir la queue, colocamos el siguiente parametro al definir el "channel.basic_consume(queue=$name_queue,on_message_callback=$method, auto_ack=True)"

