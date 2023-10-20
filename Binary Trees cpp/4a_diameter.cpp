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



// 543. Diameter of Binary Tree (Width) Diameter = Longest Path between any 2 nodes
// Optimal Approach 
pair<int, int> diameterFast(TreeNode* root) {
    if (root == nullptr) {
        return {0, 0};
    }

    auto left = diameterFast(root->left);
    auto right = diameterFast(root->right);

    int op1 = left.first;
    int op2 = right.first;
    int op3 = left.second + right.second + 1;

    int diameter = max({op1, op2, op3});
    int height = max(left.second, right.second) + 1;

    return {diameter, height};
}

int diameter(TreeNode* root) {
    return diameterFast(root).first;
}



// Approach 2
int height(TreeNode* root) {
    if (root == nullptr) {
        return 0;
    }

    int left = height(root->left);
    int right = height(root->right);

    int ans = std::max(left, right) + 1;
    return ans;
}

int diameter(TreeNode* root) {
    if (root == nullptr) {
        return 0;
    }

    int op1 = diameter(root->left);
    int op2 = diameter(root->right);
    int op3 = height(root->left) + height(root->right) + 1;

    int ans = std::max(op1, std::max(op2, op3));
    return ans;
}
