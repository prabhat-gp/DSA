// Leaf Nodes at Same Level 
int height(TreeNode* root) {
    if (root == nullptr) return 0;

    int left = height(root->left);
    int right = height(root->right);

    int ans = max(left, right) + 1;
    return ans;
}

int minDepth(TreeNode* root) {
    if (root == nullptr) return 0;
        
    int left = minDepth(root->left);
    int right = minDepth(root->right);

    if (left == 0) 
        return right + 1;
    if (right == 0) 
        return left + 1;

    int ans = min(left, right) + 1;
    return ans;
}

bool check(TreeNode* root) {
    int max_depth = height(root);
    int min_depth = minDepth(root);

    return max_depth == min_depth;
}


// Duplicate subtree in Binary Tree
// 652. Find Duplicate Subtrees 