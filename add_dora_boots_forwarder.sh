#!/bin/bash
# author: lee_xu@foxmail.com
# date: 2017-07-01
# usage: 生成 prometheus 对应服务监控

shopt -s expand_aliases
source ~/.bash_profile
NODE=$1
IP=$(lip $NODE)

echo "- targets: ['$IP:9001']
  labels:
      node: '$NODE'
      teams: 'dora'
      services: 'boots-forwarder'"
echo
