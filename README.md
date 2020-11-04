# Simple Shell


This project is a console used in creating, loading, and saving objects related to a clone of the AirBnB app.

  - Can work in interactive and non-interactive modes!
    - Includes built-in commands!
      - Saves your data to be used in the future!

      ### Installation

      Clone the repository and run the python file console.

      ```sh
      $ git clone https://github.com/not-notAlex/AirBnB_clone
      $ ./console
      ```

      Example of non-interactive use

      ```sh
      $ echo "command" | ./console
      ```

      ## Current Built-in Commands
      - quit - Terminates the console.
      - help - Lists all of the current commands.
      - create - Creates a new class with unique id. Use: create <class name>
      - show - Shows object of given class and id. Use: show <class name> <id>
      - destroy - Deletes object of given class and id. Use: destroy <class name> <id>
      - all - Shows all objects of given class. Will show ALL objects if left blank. Use: all <class name>
      - update - Updates a specific object with new attribute data. Use: <class name> <id> <attribute name> <value>

      ## Example of use
      ```sh
      (your shell)$ ./console
      (hbnb) create BaseModel
      49faff9a-6318-451f-87b6-910505c55907
      $ all BaseModel
      ["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
      $ quit
      (your shell)$
      ```

	### Authors

	-[Alex Smith]



	   [Alex Smith]: <https://github.com/not-notAlex>
