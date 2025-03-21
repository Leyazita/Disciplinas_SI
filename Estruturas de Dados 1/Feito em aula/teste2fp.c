#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NAME 50
#define MAX_ADDRESS 100
#define MAX_ATTEMPTS 3

typedef struct Client {
  char name[MAX_NAME];
  char address[MAX_ADDRESS];
  int attempts;
  struct Client *next;
} Client;

typedef struct Delivery {
  Client *client;
  struct Delivery *next;
} Delivery;

typedef struct Return {
  Client *client;
  struct Return *next;
} Return;

typedef struct Score {
  float score;
} Score;

Client *createClient(char *name, char *address) {
  Client *client = (Client*) malloc(sizeof(Client));
  strcpy(client->name, name);
  strcpy(client->address, address);
  client->attempts = 0;
  client->next = NULL;
  return client;
}

Delivery *createDelivery(Client *client) {
  Delivery *delivery = (Delivery*) malloc(sizeof(Delivery));
  delivery->client = client;
  delivery->next = NULL;
  return delivery;
}

Return *createReturn(Client *client) {
  Return *returnItem = (Return*) malloc(sizeof(Return));
  returnItem->client = client;
  returnItem->next = NULL;
  return returnItem;
}

void insertClient(Client **head, Client *client) {
  Client *current = *head;
  if(*head == NULL) {
    *head = client;
  } else {
    while(current->next != NULL) {
      current = current->next;
    }
    current->next = client;
  }
}

void enqueueDelivery(Delivery **head, Delivery *delivery) {
  Delivery *current = *head;
  if(*head == NULL) {
    *head = delivery;
  } else {
    while(current->next != NULL) {
      current = current->next;
    }
    current->next = delivery;
  }
}

Delivery *dequeueDelivery(Delivery **head) {
  Delivery *delivery = *head;
  *head = (*head)->next;
  return delivery;
}

void pushReturn(Return **head, Return *returnItem) {
  returnItem->next = *head;
  *head = returnItem;
}

Return *popReturn(Return **head) {
  Return *returnItem = *head;
  *head = (*head)->next;
  return returnItem;
}

void updateScore(Score *score, Delivery *delivery) {
  if(delivery->client->attempts == 0) {
    score->score += 5;
  } else if(delivery->client->attempts == 1) {
    score->score += 3;
  } else if(delivery->client->attempts == 2) {  
    score->score += 2;
  }
  //entrega nao realizada -0,8
  else {
    score->score -= 0.8;
  }
}

