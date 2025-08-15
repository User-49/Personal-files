// Implementation of binary search tree


struct node{
    int data;
    struct node *left;
    struct node *right;
} *head=NULL;

void preorder(struct node*);
void postorder(struct node*);
void inorder(struct node*);
int add(int data,struct node*);


void main(){
    int choice, data;
    do{
        printf("\n-------------------------------------------");
        printf("1. Inorder traversal\n");
        printf("2. preorder traversal\n");
        printf("3. postorder traversal\n");
        printf("4. add item");
        printf("Enter choice: ");
        scanf(" %d",&choice);

        switch(choice){
            case 1:
                inorder(head);
                break;
            case 2:
                preorder(head);
                break; 
            case 3:
                postorder(head);
                break;
            case 4:
                printf("\nEnter the item: ");
                scanf(" %d", &data);
                if(add(data)) printf("Data added sucessfully");
                else printf("Memory allocation faliure- data not added");
                break;
            default:
                printf("\n Invalid choice");
        }

    }while(1);
}


void preorder(struct node *node){
    if (node){
        printf("%d, ", node->data);
        preorder(node->left);
        preorder(node->right);
    }
}


void postorder(struct node *node){
    if (node){
        printf("%d, ", node->data);
        postorder(node->left);
        postorder(node->right);
    }
}


void inorder(struct node *node){
    if (node){
        printf("%d, ", node->data);
        inorder(node->left);
        inorder(node->right);
    }
}


int add(int data,struct *node){
    if (data > node->data)
        if (node->right)
            add(data,node->right);
        else{
            node->right = (struct node*)malloc(sizeof(struct node));
            if (!(node->right)) return 0;
            *(node->right) = (struct node){data, NULL,NULL};
        }
    else
        if (node->left)
            add(data, node->left);
        else{
            node->left = (struct node*)malloc(sizeof(struct node));
            if (!(node->left)) return 0;
            *(node->left) = (struct node){data, NULL,NULL};
        }
            
}
