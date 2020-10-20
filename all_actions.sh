#!/usr/bin/env bash

for i in stdlib numpy pandas pytorch scipy h5py sphinx attrs sarge django
do
  ./action.sh $i $1
done

