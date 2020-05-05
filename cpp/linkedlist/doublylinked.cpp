#include<bits/stdc++.h>
using namespace std;
struct node{
    int data;
    struct node *next;
    struct node *prev;
};
struct node *head=NULL;


void insertEnd() 
{   long long int value;
    cout<<"\nEnter the value to be inserted:";
    cin>>value;
    // If the list is empty, create a single node 
    // circular and doubly list 
    if (*head == NULL) 
    { 
        struct Node* new_node = new Node; 
        new_node->data = value; 
        new_node->next = new_node->prev = new_node; 
        *head = new_node; 
        return; 
    } 
  
    // If list is not empty 
  
    /* Find last node */
    Node *last = (*head)->prev; 
  
    // Create Node dynamically 
    struct Node* new_node = new Node; 
    new_node->data = value; 
  
    // Start is going to be next of new_node 
    new_node->next = *head; 
  
    // Make new node previous of start 
    (*head)->prev = new_node; 
  
    // Make last preivous of new node 
    new_node->prev = last; 
  
    // Make new node next of old last 
    last->next = new_node; 
} 


void append()
{
    struct node *t;
    t=head;
    int c,data;
    cout<<"\nEnter the node after which you want to insert another node:";
    cin>>c;
    cout<<"\nEnter data to be inserted";
    cin>>data;
    struct node *newnode=(struct node*)malloc(sizeof(struct node));
    newnode->data=data;
    newnode->next=NULL;
    newnode->prev=NULL;
    for(int i=1;i<c;i++)
    {
        t=t->next;
    }
    newnode->prev=t;
    newnode->next=t->next;
    t->next->prev=newnode;
    t->next=newnode;
   
   
   
   
}


void Insert()
{
    int data;
cout<<"\nEnter the data for new node:";
cin>>data;
    struct node *newnode=(struct node*)malloc(sizeof(struct node));
    newnode->data=data;
    newnode->prev=NULL;
    if(head!=NULL)
    {
        newnode->next=head;
        head->prev=newnode;
    }
    head=newnode;
}

void deleted()
{
    struct node *p;
    p=head;
    p->next->prev=NULL;
    head=p->next;
    free(p);
}

void traverse()
{
    struct node *t;
    t=head;
    while(t!=NULL)
    {
        cout<<t->data<<" ";
        t=t->next;
    }

    cout<<endl;
}

void selectionSort()
{
    struct node* temp = head;
 
    while (temp) {
        struct node* min = temp;
        struct node* r = temp->next;
        while (r) {
            if (min->data > r->data)
                min = r;
            r = r->next;
        }
        int x = temp->data;
        temp->data = min->data;
        min->data = x;
        temp = temp->next;
    }
}

int main()
{int ch;
ch=5;
while(ch!=0){
cout<<"1.Insert Node "<<endl;
cout<<"2.Delete Node"<<endl;
cout<<"3.Print the list"<<endl;
cout<<"4.Append"<<endl;
cout<<"5.Sort"<<endl;
cout<<"0.Exit"<<endl;
label:
cin>>ch;
switch(ch)
{
    case 1: Insert();
            break;
    case 2: deleted();
            break;
    case 3: traverse();
            break;
    case 4: append();
            break;
    case 5: selectionSort();
    break;
}
            }
    return 0;
}
