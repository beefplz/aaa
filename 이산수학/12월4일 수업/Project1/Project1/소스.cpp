#include<iostream>
using namespace std;
struct node {
	int key;
	struct node* left, * right;
};
struct node* newNode(int item) {
	struct node* temp = (struct node*)malloc(sizeof(struct node));
	temp->key = item;
	temp->left = temp->right = NULL;
	return temp;
}
struct node* insert(struct node* node, int key) {
	if (node == NULL) {
		return newNode(key);
	}
	if (key < node->key) {
		node->left = insert(node->left, key);
	}
	else if (key > node->key) {
		node->right = insert(node->right, key);
	}
	return node;
}
void inorder(struct node* root) {
	if (root != NULL) {
		inorder(root->left);
		printf("%d\n", root->key);
		inorder(root->right);
	}
}
void preOrder(struct node* root) {
	if (root != NULL) {
		printf("$d\n", root->key);
		preOrder(root->left);
		preOrder(root->right);
	}
}

void postOrder(struct node* root) {
	if (root != NULL) {
		postOrder(root->left);
		postOrder(root->right);
		printf("%d\n", root->key);
	}
}
int main() {
	struct node* root = NULL;
	root = insert(root, 50);
	insert(root, 30);
	insert(root, 20);
	insert(root, 40);
	insert(root, 70);
	insert(root, 60);
	insert(root, 80);
	cout << "in order" << endl;
	inorder(root);
	cout << "pre order" << endl;
	preOrder(root);
	cout << "post order" << endl;
	postOrder(root);
	return 0;
}