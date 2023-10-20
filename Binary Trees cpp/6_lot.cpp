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

// 102. Binary Tree Level Order Traversal
vector<int> levelOrderTraversal(TreeNode* root) {
    vector<int> res;
    if (root == nullptr) {
        return res;
    }

    queue<TreeNode*> q;
    q.push(root);

    while (!q.empty()) {
        TreeNode* curr = q.front();
        q.pop();
        res.push_back(curr->val);

        if (curr->left) {
            q.push(curr->left);
        }

        if (curr->right) {
            q.push(curr->right);
        }
    }

    return res;
}



// 107. Binary Tree Level Order Traversal (Reverse LOT)

// 637. Average of Levels in Binary Tree


// 958. Check Completeness of a Binary Tree



// 1161. Maximum Level Sum of Binary Tree  (Maximum Sum or Maximum Level of Binary Tree (both))


// 2583. kth Largest Sum in Binary Tree
