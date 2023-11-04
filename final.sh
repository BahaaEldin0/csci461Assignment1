#!/bin/bash

cotainer_id=$(sudo docker ps -l -q)

sudo docker cp "$cotainer_id":/home/doc-bd-a1/res_dpre.csv service-result
sudo docker cp "$cotainer_id":/home/doc-bd-a1/eda-in-1.txt service-result
sudo docker cp "$cotainer_id":/home/doc-bd-a1/eda-in-2.txt service-result
sudo docker cp "$cotainer_id":/home/doc-bd-a1/eda-in-3.txt service-result
sudo docker cp "$cotainer_id":/home/doc-bd-a1/vis.png service-result
sudo docker cp "$cotainer_id":/home/doc-bd-a1/k.txt service-result

sudo docker container stop "$container_id"
