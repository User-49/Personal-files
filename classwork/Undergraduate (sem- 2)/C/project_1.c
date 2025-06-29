#include <stdio.h>
#include <stdlib.h>
struct node{
	int data;
	struct node * link;
}*head=NULL,*temp=NULL;


int insertBegining(struct node**, int);
int insertIndex(struct node**, int, int);



int insertBegining(struct node **head_ptr, int data){
	temp = (struct node *)malloc(sizeof(struct node));
	if (temp == NULL) return 1;
	*temp = (struct node){data,(*head_ptr)->link};
	*head_ptr = temp;
	return 0;
}


int insertIndex(struct node **head_ptr,int data,int index){
	if (!index) return insertBegining(head_ptr,data);
	for (int i=0;i<index;i++){
		if ((*head_ptr)->link==NULL) return 1;
		*head_ptr = (*head_ptr)->link;
	}
	if ((temp = (struct node*)malloc(sizeof(struct node)))==NULL) return 1;
	*temp = (struct node){data,(*head_ptr)->link};
	(*head_ptr)->link = temp;
	return 0;
}


int append(struct node *head,int data){
	while (head->link!=NULL) head = head->link;
	if ((head->link = (struct node *)malloc(sizeof(struct node)))==NULL) return 1;
	*(head->link) = (struct node){data, NULL};
	return 0;
}

int traverse(struct node *head){
	int count = 0;
	while (head!=NULL){
		printf("%d, ",head->data);
		head=head->link;
		count++;
	}
	return count;
}



void main(){
int choice,data,index;

do{
printf("\n--------------------------------------------------------------");
printf("\nwhat do you wish to do..?");
printf("\n1. Append List");
printf("\n2. Traverse List");
printf("\n3. Insert at Begining");
printf("\n4. Insert at index");
printf("\n0. Exit");

printf("\nenter choice: ");
scanf("%d", &choice);

switch (choice){
	case 1:
		printf("\nEnter the element: ");
		scanf("%d",&data);
		if (!append(head,data)) printf("\n--memory allocation failed--");
		break;
	case 2:
		traverse(head);
		break;
	case 3:
		printf("\nEnter the element: ");
		scanf("%d",&data);
		if (insertBegining(&head,data)== 1) printf("\n---memory allocation failed--");
		break;
	case 4:
		printf("\nEnter the element: ");
		scanf("%d",&data);
		printf("\nEnter the index: ");
		scanf("%d",&index);
		if (insertIndex(&head,data,index)) printf("\n--memory alllocation failed--");
		break;
	case 0:
		printf("you have exited the program");
		break;
	default:
		printf("\n---invalid input---");
}
}while(choice);	
}
