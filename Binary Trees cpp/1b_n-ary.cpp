// N-ary Tree 
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};



// 589. N-ary Tree Preorder Traversal 
void preorderTraversal(Node* node, vector<int>& result) {
    if (node == nullptr) {
        return;
    }
        
    result.push_back(node->val);
        
    for (Node* child : node->children) {
        preorderTraversal(child, result);
    }
}

vector<int> preorder(Node* root) {
    vector<int> result;
    preorderTraversal(root, result);
    return result;
}
    


// 590. N-ary Tree Postorder Traversal 
void postorderTraversal(Node* node, vector<int>& result) {
    if (node == nullptr) {
        return;
    }
        
    for (Node* child : node->children) {
        postorderTraversal(child, result);
    }  
    result.push_back(node->val);
}

vector<int> postorder(Node* root) {
    vector<int> result;
    postorderTraversal(root, result);
    return result;
}
    



// 559. Maximum Depth of N-ary Tree 
int maxDepth(Node* root) {
    if (root == nullptr) {
        return 0;
    }

    int maxChildDepth = 0;
    for (Node* child : root->children) {
        maxChildDepth = max(maxChildDepth, maxDepth(child));
    }

    return maxChildDepth + 1; 
}
