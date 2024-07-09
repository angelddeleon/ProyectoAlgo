#El programa deberá gestionar(crear, listar,modificar, consultar y listar) las
#empresas clientes con todos sus datos relevantes(id, nombre, descripción,
#fecha_creación, dirección,teléfono, correo, gerente,
#equipo_contacto). Esto incluye la creación, modificación, consulta, eliminación y
#listado de las empresas clientes, garantizando una organización eficiente y
#accesible. A continuación, se detallan las funcionalidades específicas requeridas
#para la gestión de empresas clientes. Los datos de las empresas clientes deberán
#guardarse en un archivo csv que será cargado al inicio del programa en una lista
#enlazada. Adicionalmente cada empresa cliente tendrá asociado 1 o mas proyectos
#el cual podrán ser gestionados al seleccionar un cliente especifico

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkendList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)
    
    def find(self, targetValue):
        current = self.head
        while current:
            if current.value.id == targetValue:
                return current.value
            current = current.next
        return False
        
    def delete(self, target_value):
        prev = None
        current = self.head
        while current:
            if current.value == target_value:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                current.next = None
                return
            prev = current
            current = current.next
        
            
    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)
        elif value.time_remaining < node.value.time_remaining:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        node.height = 1 + max(self._height(node.left), self._height(node.right))

        balance = self._balance(node)

        if balance > 1:
            if value.time_remaining < node.left.value.time_remaining:
                return self._right_rotate(node)
            else:
                node.left = self._left_rotate(node.left)
                return self._right_rotate(node)

        if balance < -1:
            if value.time_remaining > node.right.value.time_remaining:
                return self._left_rotate(node)
            else:
                node.right = self._right_rotate(node.right)
                return self._left_rotate(node)

        return node

    def _height(self, node):
        if node is None:
            return 0
        return node.height

    def _balance(self, node):
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        return y

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        return y

class Project:
    def __init__(self, id, name, description, start_date, end_date, status, company, manager, team):
        self.id = id
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.company = company
        self.manager = manager
        self.team = team
        self.time_remaining = self.calculate_time_remaining()

    def calculate_time_remaining(self):
        # calculate time remaining based on current date and end date
        pass



class Client:
    def __init__(self, id, name, description, creationDate, direction, phone, mail, manager, contactTeam):
        self.id = id
        self.name = name
        self.description = description
        self.creationDate = creationDate
        self.direction = direction
        self.phone = phone
        self.mail = mail
        self.manager = manager
        self.contactTeam = contactTeam
        self.projects = AVLTree()
        
    def modify(self, id, name, description, creationDate, direction, phone, mail, manager, contactTeam):
        self.id = id
        self.name = name
        self.description = description
        self.creationDate = creationDate
        self.direction = direction
        self.phone = phone
        self.mail = mail
        self.manager = manager
        self.contactTeam = contactTeam
        
    def __str__(self):
        return f"{self.id}, {self.name} {self.description} {self.creationDate} {self.direction} {self.phone} {self.mail} {self.manager} {self.contactTeam}"

    def add_project(self, project):
        self.projects.insert(project)

    ##########################CAMBIAR##########################
    
    def modify_project(self, criteria, value , new_data):
        project = self.search_project(criteria, value)
        if project:
            project.name = new_data.get('name', project.name)
            project.description = new_data.get('description', project.description)
            project.start_date = new_data.get('start_date', project.start_date)
            project.end_date = new_data.get('end_date', project.end_date)
            project.status = new_data.get('status', project.status)
            project.company = new_data.get('company', project.company)
            project.manager = new_data.get('manager', project.manager)
            project.team = new_data.get('team', project.team)
            project.time_remaining = project.calculate_time_remaining()
            self.projects = AVLTree()  # rebuild the AVL tree
            for p in self.get_projects():
                self.projects.insert(p)
        else:
            print("No existe el proyecto")

    def find_project(self, project_id):
        for project in self.get_projects():
            if project.id == project_id:
                return project
        return None

    def get_projects(self):
        projects = []
        self._get_projects(self.projects.root, projects)
        return projects

    def _get_projects(self, node, projects):
        if node:
            self._get_projects(node.left, projects)
            projects.append(node.value)
            self._get_projects(node.right, projects)
            
    def list_projects(self):
        for project in self.get_projects():
            print(f"ID: {project.id}, Name: {project.name}, Description: {project.description}, Start Date: {project.start_date}, End Date: {project.end_date}, Status: {project.status}, Company: {project.company}, Manager: {project.manager}, Team: {project.team}")

    def search_project(self, criteria, value):
        for project in self.get_projects():
            if criteria == 'id' and project.id == value:
                return project
            elif criteria == 'name' and project.name == value:
                return project
            elif criteria == 'manager' and project.manager == value:
                return project
            elif criteria == 'start_date' and project.start_date == value:
                return project
            elif criteria == 'end_date' and project.end_date == value:
                return project
            elif criteria == 'status' and project.status == value:
                return project
        return None

    def delete_project(self, project_id):
        project = self.find_project(project_id)
        if project:
            self.projects = AVLTree()  # rebuild the AVL tree
            for p in self.get_projects():
                if p.id != project_id:
                    self.projects.insert(p)
            
projectList = LinkendList()

class Program:
    def __init__(self):
        self.listClients = LinkendList()

    def menuGeneral(self):
        print("1.Modulo Gesion Empresas\n2.Modulo Gestion de Proyectos\n3. Salir")

    def menuGestionEmpresa(self):
        print("1.Crear un cliente\n2.Modificar Cliente\n3.Imprimir la lista\n4. Salir")
        
    def menuGestionProyecto(self):
        print("1.Crear un Proyecto\n2.Modificar Proyecto\n3.Imprimir la lista\n4.Eliminar Proyecto\n5. Salir")    

    def createClient(self):
        id = input("Ingrese un id: ")
        name = input("Ingrese un nombre: ")
        description = input("Ingrese una descripcion: ")
        creationDate = input("Ingrese el dia de creacion del cliente: ")
        direction = input("Ingrese una direccion: ") 
        phone = input("Ingrese un numero de telefono: ") 
        mail = input("Ingrese un email: ") 
        manager = input("Ingrese un Gerente: ") 
        contactTeam = input("Ingrese el contacto del equipo: ")
        
        newClient = Client(id, name, description, creationDate, direction, phone, mail, manager, contactTeam)
        self.listClients.append(newClient)
        
    def createProject(self):
        id = input("Ingrese un id: ")
        name = input("Ingrese un nombre: ")
        description = input("Ingrese una descripcion: ")
        start_date = input("Ingrese el dia de creacion del cliente: ")
        end_date = input("Ingrese una direccion: ") 
        status = input("Ingrese un numero de telefono: ") 
        company = input("Ingrese un email: ") 
        manager = input("Ingrese un Gerente: ") 
        team = input("Ingrese el contacto del equipo: ")
        
        newProject = Project(id, name, description, start_date, end_date, status, company, manager, team)
        self.listClients.add_project(newProject)
        print("Se ha creado el proyecto")
        
    def modifyProject(self):
        print("\nn1.Id,")
        
        criteria = input("Ingrese el criterio del proyecto a modificar: ")
        value = input("Ingrese el valor del proyecto a modificar: ")
        project = self.listClients.search_project(criteria, value)
        
        if project:
            name = input("Ingrese un nombre: ")
            description = input("Ingrese una descripcion: ")
            start_date = input("Ingrese el dia de creacion del cliente: ") 
            end_date = input("Ingrese la fecha de fin del proyecto: ")
            status = input("Ingrese el estado del proyecto: ")
            company = input("Ingrese la empresa del proyecto: ")
            manager = input("Ingrese el gerente del proyecto: ")
            team = input("Ingrese el equipo del proyecto: ")
            
            new_data = {
                "name": name,
                "description": description,
                "start_date": start_date,
                "end_date": end_date,
                "status": status,
                "company": company,
                "manager": manager,
                "team": team
            }
            self.listClients.modify_project(id, new_data)
        else:
            print("Proyecto no encontrado")

    def print_project_list(self):
        id = input("Ingrese el id del cliente que desea ver sus proyectos: ")
        
        client = self.listClients.find(id)
        if client:
            client.list_projects()
        else:
            print("Cliente no encontrado")
    
    def deleteProject():
        
        id = input("Ingrese el id del proyecto que desea eliminar: ")
        
        self.listClients.delete_project(id)
        
        print("Su proyecto ha sido eliminado")
    
    def program(self):
        while True:
            self.menuGeneral()
            opcionMenunGeneral = int(input("Escoge a que modulo desea acceder: "))
            
            if opcionMenunGeneral == 1:
                while True:
                    self.menuGestionEmpresa()
                    opcion = int(input("Ingrese una opcion: "))
                    if opcion == 1:
                        self.createClient()
                    elif opcion == 2:
                        id = input("Ingrese un numero: ")
                        element = self.listClients.find(id)
                        
                        if element:
                            name = input("Ingrese un nuevo nombre: ")
                            description = input("Ingrese una nueva descripcion: ")
                            creationDate = input("Ingrese una nueva fecha de creacion: ")
                            direction = input("Ingrese una nueva direccion: ") 
                            phone = input("Ingrese un nuevo numero de telefono: ") 
                            mail = input("Ingrese un nuevo email: ") 
                            manager = input("Ingrese un nuevo Gerente: ") 
                            contactTeam = input("Ingrese un nuevo contacto del equipo: ")
                            element.modify(id, name, description, creationDate, direction, phone, mail, manager, contactTeam)
                            
                            self.menuGestionEmpresa()
                
                            opcion = int(input("Ingrese una opcion: "))
                            
                        else:
                            print("Cliente no encontrado")
                            
                            Program.menuGestionEmpresa()
                
                            opcion = int(input("Ingrese una opcion: "))
                            
                    elif opcion == 3:
                        self.listClients.print_list()
                        
                        self.menuGestionEmpresa()
                
                        opcion = int(input("Ingrese una opcion: "))
                        
                    elif opcion == 4:
                        break  # Salir del menú de gestión de empresa
                    else:
                        print("Opción inválida. Intente de nuevo.")
                        
                
            #Menu de Proyectos
            
            elif opcionMenunGeneral == 2:
                
                print("1.Crear un Proyecto\n2.Modificar Proyecto\n3.Imprimir la lista\n4.Eliminar Proyecto\n5. Salir")    
                
                opcionMenuProyecto = input("Ingrese su opcion: ")
                
                if opcionMenuProyecto == 1:
                    
                    self.createProject()
                    
                    print("1.Crear un Proyecto\n2.Modificar Proyecto\n3.Imprimir la lista\n4.Eliminar Proyecto\n5. Salir")    
                
                    opcionMenuProyecto = input("Ingrese su opcion: ")
                    
                elif opcionMenuProyecto == 2:    
                    
                    self.modifyProject()
                    
                    print("1.Crear un Proyecto\n2.Modificar Proyecto\n3.Imprimir la lista\n4.Eliminar Proyecto\n5. Salir")    
                
                    opcionMenuProyecto = input("Ingrese su opcion: ")
                    
                elif opcionMenuProyecto == 3:
                    
                    self.print_project_list()
                    
                    print("1.Crear un Proyecto\n2.Modificar Proyecto\n3.Imprimir la lista\n4.Eliminar Proyecto\n5. Salir")    
                
                    opcionMenuProyecto = input("Ingrese su opcion: ")
                    
                elif opcionMenuProyecto == 4:
                    
                    self.deleteProject()
                    
                    print("1.Crear un Proyecto\n2.Modificar Proyecto\n3.Imprimir la lista\n4.Eliminar Proyecto\n5. Salir")    
                
                    opcionMenuProyecto = input("Ingrese su opcion: ")
                    
            elif opcionMenunGeneral == 3:
                print("Saliendo del bucle")
                
                break       
            
            else:
                print("Opcion No valida")
                
                
                 
program_instance = Program()
program_instance.program()