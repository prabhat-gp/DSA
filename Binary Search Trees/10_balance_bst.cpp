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


// 1382. Balance a Binary Search Tree (Normal BST to Balanced BST)
void inorder(TreeNode* root, vector<int>& ans) {
    if(root == nullptr) return;

    inorder(root->left, ans);
    ans.push_back(root->val);
    inorder(root->right, ans);
}

TreeNode* solve(int start, int end, vector<int>& ans) {
    if (start > end) return NULL;
    int mid = start + (end - start) / 2;
    TreeNode* root = new TreeNode(ans[mid]);
    root->left = solve(start, mid - 1, ans);
    root->right = solve(mid + 1, end, ans);
    return root;
}

TreeNode* buildBalancedTree(TreeNode* root) {
    vector<int> ans;
    inorder(root, ans);
    return solve(0, ans.size() - 1, ans);
}



