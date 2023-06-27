# Practicas Python

## 1. Indice
* [Buenas Practicas](#2-buenas-practicas)
* [Estructura del proyecto](#3-estructura-del-proyecto)
* [Eso del git](#4-uso-de-git)
* [Extensiones recomendadas](#5-extenciones-recomendadas)
* [Configuracion adicional](#6-configuracion-adicional)

## 2. Buenas practicas
Las buenas practicas son hechas para facilitar la lectura del codigo y tener mejor estructurado el codigo por lo que estas seran aquellas que en este prollecto se seguirán

1. Variables y funciones deben ser nombradas o en camelCase o snakeCase pero se debe de seguir el patron
2. Clases siempre deben ser nombradas en PascalCase
3. Cada nuevo proyecto debra ser trabajado en una rama nueva el la cual la primera palabra debera llevar como prefijo feature-, update- o enhancement- mas el nombre de la rama, ejemplo *update-readme* o *feature-ogro*
4. en la estructuracion del codigo tener en cuenta las siguientes reglas de python

	* el espacio antes de una funcion debe ser de 2 saltos de linea y despues de una debe ser de 1 salto de linea
	* las importaciones son las primeras cosas en ser instanciadas en orden alfabetico, luego les sigen las variables globales con 1 salto de linea ante de ser instanciadas y 1 salto de linea al terminar su instanciamiento
	* *ciclos for, if, while, match* deben tener un salto de linea antes de ser instanciados y despues de ser instanciados a menos que sean el primer recuso llamado dentro de una funcion
	* antes de un *return* siempre debe existir un salto de linea
	* para ejecutar la logica del codigo usar funcion de if name
	* la tabulacion de python debera ser de 4 espacios
	* las variables deben llevar nombres referentes a lo que guardan como  las funciones a lo que hacen
	* las funciones deben indicar que retornar

## 3. Estructura del proyecto
Para cada ejercicio debera ir dentro de un directorio nuevo con un nombre que haga referencia al ejercicio que se esta trabajando. Dentro del directorio debera existir un archivo principal llamado main el cual ejecutara toda la logica del sistema, y en caso de estar trabajando con un podelo *POO* tener cada subdirectorio necesario, pero main debe estar en la ruta absoluta del proyecto

## 4. Uso de git

1. Para inicializar un proyecto se usa el comando **git init**, lo que hara es que comenzara a versionar todo el proyecto desde el momento que se inicializa, pero no necesariamente estara vinculado a un proyecto en linea
	```bash
	git init
	```

2. Para la creacion de ramas se usara el comando **git checkout -b nombrerama**, este comando al ejecutarse se encargara de crear la nueva rama como lo haria **git branch nombreRama** pero luego nos cambia a ella
	```bash
	git checkout -b nombreRama
	```

3. Para cambiar entre ramas o moverse, se utiliza el comando **git checkout nombreRama**, y esta te cambiara entre ellas
	```bash
	git checkout nombreRama
	```

3. Para guardar agregar cambios primero se deben visualizar los cambios realizados en una consola con el comando **git status**, este comando mostrara en color rojo todos los archivos que han sufrido alguna modificacion o en verde todos los archivos que han sido modificado y agregado pero no guardados
	```bash
	git status
	```

4. Para agregar los cambios de archivos se utiliza **git add** con un * si se pretende agregar todos los archivos menos los ocultos que comienzan con . o usar un . para agregar todos los archivos incluso los ocultos
	```bash
	git add *
	```

5. Posteriormente a agregar los cambios de los archivos, se deben guardar los cambios con el comando **git commit -m "mensaje"**, pero ante de hacer cualquier commit, se debe verificar que con **git status** que este todo en verde lo que se desea guardar ya que lo que este en rojo no se incorporara dentro del commit
	```bash
	git commit -m "mensaje"
	```

6. Si se esta trabajando con un repositorio en linea ya sea en github o gitlab, o el que sea se necesitara subir los cambios guarados por el commit con el comando **git push origin nombreRama**, jamas se debe hacer un push al origin main, siembre al la misma rama al que se esta trabajando
	```bash
	git push origin nombreRama
	```

7. Si existe algun cambio en alguna rama en la nube y se desea traer al local, se debe realizar con el comando **git pull origin nombreRama**, este comando traera los ultimos cambio de la rama que se le indique a la rama en la que se esta actualmente, generalmente se trae los cambios de main a la rama que uno trabaja y a main, pero al usar **git pull** traera todos los cambios y todas las ramas online
	```bash
	git pull origin main
	```

8. Si se desea clonar un proyecto en linea, se utiliza el comando **git clone link** y traera el proyecto completo a la posicion de la consola
	```bash
	git clone git@github.com:vk-7/coffe.gitgit@github.com:vk-7/coffe.git
	```

## 5. Extenciones recomendadas
EditorConfig.EditorConfig

aaron-bond.better-comments

eamodio.gitlens

donjayamanne.githistory

PKief.material-icon-theme

christian-kohler.path-intellisense

Shan.code-settings-sync

shardulm94.trailing-spaces

adpyke.vscode-sql-formatter

esbenp.prettier-vscode

## 6. Configuracion adicional
Dentro de las configuraciones de vscode recomiendo hacer las siguientes

1. instalar un autoformateador, el cual hara que el codigo se mantenga de manera prolija, para ello recomiendo la instalacion de autopep8. En python para instalar paquetes adicionales o addons, se usa el siguiente comando
	```bash
	pip install autopep8 -> linux
	python -m pip install autopep8 -> windows
	```

2. Dentro de las configuraciones json del vscode agregar el siguiente codigo
	```json
	"[python]": {
        "gitlens.codeLens.symbolScopes": ["!Module"],
        "editor.wordBasedSuggestions": false,
        "editor.defaultFormatter": "ms-python.python"
	```
	y posteriormente dentro de los atajos de teclado configurar el autoformater con las teclas **alt + x**

Dentro de las configuraciones del usuario, asegurarse que las siguiente opciones contengan los siguientes parametros

1. python > formatting: provaider

	autopep8

En caso de necesitar las rutas en donde python guarda los addons es: **C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python310\Scripts**
