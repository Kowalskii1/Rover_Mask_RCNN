from setuptools import setup, find_packages

setup(
    name='Rover_Mask_RCNN',  # Nombre del paquete
    version='0.1',           # Versión del paquete
    packages=find_packages(),  # Encuentra automáticamente todos los paquetes Python
    install_requires=[        # Dependencias necesarias
        'numpy',              # Puedes añadir cualquier otra librería que utilices
        'tensorflow',
        'keras',
        # Otras dependencias si las tienes
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',  # La versión mínima de Python que soportas
)
