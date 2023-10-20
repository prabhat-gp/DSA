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


// 104. Height of Binary Tree (Max Depth)
int height(TreeNode* root) {
    if (root == nullptr) {
        return 0;
    }

    int left = height(root->left);
    int right = height(root->right);

    int ans = max(left, right) + 1;
    return ans;
}



// 111. Min Depth of Binary Tree
int minDepth(TreeNode* root) {
    if (root == nullptr) {
        return 0;
    }

    int left = minDepth(root->left);
    int right = minDepth(root->right);

    if (left == 0) {
        return right + 1;
    }
    if (right == 0) {
        return left + 1;
    }

    int ans = min(left, right) + 1;
    return ans;
}



// Leaf Nodes at Same Level 
bool check(TreeNode* root) {
    int max_depth = height(root);
    int min_depth = minDepth(root);

    return max_depth == min_depth;
}



// 814. Binary Tree Pruning
TreeNode* pruneTree(TreeNode* root) {
    if (root == nullptr) {
        return nullptr;
    }

    root->left = pruneTree(root->left);
    root->right = pruneTree(root->right);

    if (root->left == nullptr && root->right == nullptr && root->val == 0) {
        return nullptr;
    }

    return root;
}


// Duplicate subtree in Binary Tree
// 652. Find Duplicate Subtrees 