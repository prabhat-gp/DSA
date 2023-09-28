// 98. Valiate Binary Search Tree 

// Properties of BST 
// * For every node, left subtree has values less that root and right subtree has values greater than root. 
// * Inorder Traversal is sorted


struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int val) {
        this->val = val;
        this->left = NULL;
        this->right = NULL;
    }
}


bool solve(TreeNode* root, int minVal, int maxVal) {
    if(root == nullptr) return true;

    if(root->val > min && root->val < max) {
        bool left = solve(root->left, min, root->val);
        bool right = solve(root->right, root->val, max);
        return left && right;
    }

    return false;
}

bool isValidBST(TreeNode* root) {
    return solve(root, INT_MIN, INT_MAX);
}


// LCA in BST 
// Find common nodes in two BSTs 