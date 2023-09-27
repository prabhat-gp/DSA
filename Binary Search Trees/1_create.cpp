#include <iostream>
#include <queue> // Include the queue header
using namespace std;

class Node {
public:
    int data;
    Node* left;
    Node* right;

    Node(int data) {
        this->data = data;
        this->left = NULL;
        this->right = NULL;
    }
};

Node* insertIntoBST(Node* &root, int data) {
    if (root == NULL) {
        root = new Node(data);
        return root;
    }

    if (data > root->data) {
        root->right = insertIntoBST(root->right, data);
    } else {
        root->left = insertIntoBST(root->left, data);
    }

    return root;
}

void takeInput(Node* &root) {
    int data;
    cin >> data;

    while (data != -1) {
        insertIntoBST(root, data);
        cin >> data;
    }
}

void levelOrderTraversal(Node* root) {
    queue<Node*> qu;
    qu.push(root);
    qu.push(NULL);

    while (!qu.empty()) {
        Node* temp = qu.front();
        qu.pop();

        if (temp == NULL) {
            cout << endl;
            if (!qu.empty()) {
                qu.push(NULL);
            }
        } else {
            cout << temp->data << " ";
            if (temp->left) {
                qu.push(temp->left);
            }

            if (temp->right) {
                qu.push(temp->right);
            }
        }
    }
}

int main() {
    Node* root = NULL;

    cout << "Enter data to create BST" << endl;
    takeInput(root);

    cout << "Level Order Traversal:" << endl;
    levelOrderTraversal(root);

    return 0;
}

// Insertion T.C = O(logN)