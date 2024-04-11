"""

Necessary for Keymaster's Database
This code was written by echo complex (https://t.me/echoscomplex)
License - GNU GPLv2 Keymaster's © 2024 (CEO - echo complex (https://t.me/echoscomplex))
All rights reserved.


What is this?

This file is needed to run everything needed for the database,
and specifically to start/shutdown the JVM (Java Virtual Machine) before/after it runs, since the database logic is written in Java.

"""


from jpype import startJVM, shutdownJVM
from os import getcwd


def startDatabase () -> None:
    # Starting JVM
    startJVM(classpath=([
        ('%s/Database/DatabaseClassesJava/' % getcwd()),
        ('%s/Database/DatabaseClassesJava/lib/sqlite-jdbc-3.45.2.0.jar' % getcwd()),
        ('%s/Database/DatabaseClassesJava/lib/slf4j-api-2.0.9.jar' % getcwd()),
        ('%s/Database/DatabaseClassesJava/lib/slf4j-simple-2.0.9.jar' % getcwd())])
    );

def shutdownDatabase () -> None:
    shutdownJVM();  # Shutdown JVM
