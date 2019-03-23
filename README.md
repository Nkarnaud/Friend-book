Flask restful api with blueprint and docker

This application is a crud for a user wsith the following functionalitie
1- Users should be able to create a password-protected profile
2- Users should be able to log in to their profile
3- Users should be able to search other users and list the results
4- Users should be able to add/remove other users as friends

How to run the App!

Install Docker version 18.06.1-ce, build e68fc7a
Install docker-compose version 1.22.0, build f46880fe
Install docker-machine version 0.14.0, build 89b8332

\$ cd to the project directory/

docker-machine create -d virtualbox currency(docker machine name)
docker-machine env currency(docker machine name)
eval "\$(docker-machine env currency(docker machine name))"
chmod +x friens/entrypoint.sh

Build the modules and subsections using docker-compose

\$ docker-compose -f docker-compose-dev.yml up -d --build

Recreate the needed databases

\$ docker-compose -f docker-compose-dev.yml run friendbook python manage.py recreate-db

Populate the database with dummy (seed) data

\$ docker-compose -f docker-compose-dev.yml run friendbook python manage.py seed-db

Run the project

\$ docker-compose -f docker-compose-dev.yml up

to test the end point

1- http://localhost:5001/friends/add_friends
2- http://localhost:5001/friends/<id>
3- http://localhost:5001/friends/lists
2-http://localhost:5001/friends/delete/<id>
