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

// 105. Construct Binary Tree from Inorder and Preorder Traversal
TreeNode* solve(vector<int>& preorder, vector<int>& inorder, unordered_map<int, int>& inorderMap, int& preorderIndex, int inorderStart, int inorderEnd) {
    if (preorderIndex >= preorder.size() || inorderStart > inorderEnd) {
        return nullptr;
    }

    int element = preorder[preorderIndex];
    TreeNode* root = new TreeNode(element);
    int position = inorderMap[element];

    preorderIndex++;
    root->left = solve(preorder, inorder, inorderMap, preorderIndex, inorderStart, position - 1);
    root->right = solve(preorder, inorder, inorderMap, preorderIndex, position + 1, inorderEnd);

    return root;
}

TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
    unordered_map<int, int> inorderMap;
    for (int i = 0; i < inorder.size(); ++i) {
        inorderMap[inorder[i]] = i;
    }

    int preorderIndex = 0;
    return solve(preorder, inorder, inorderMap, preorderIndex, 0, inorder.size() - 1);
}




// 106. Construct Binary Tree from Inorder and Postorder Traversal
TreeNode* solve(vector<int>& inorder, vector<int>& postorder, unordered_map<int, int>& inorderMap, int& postorderIndex, int inorderStart, int inorderEnd) {
    if (postorderIndex < 0 || inorderStart > inorderEnd) {
        return nullptr;
    }

    int element = postorder[postorderIndex];
    TreeNode* root = new TreeNode(element);
    int position = inorderMap[element];

    postorderIndex--;
    root->right = solve(inorder, postorder, inorderMap, postorderIndex, position + 1, inorderEnd);
    root->left = solve(inorder, postorder, inorderMap, postorderIndex, inorderStart, position - 1);

    return root;
}

TreeNode* buildTreeFromInorderPostorder(vector<int>& inorder, vector<int>& postorder) {
    unordered_map<int, int> inorderMap;
    for (int i = 0; i < inorder.size(); ++i) {
        inorderMap[inorder[i]] = i;
    }

    int postorderIndex = postorder.size() - 1;
    return solve(inorder, postorder, inorderMap, postorderIndex, 0, inorder.size() - 1);
}
