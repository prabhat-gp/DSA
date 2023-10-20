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

//  226. Convert a BT to its mirror (Invert of BT)
// Approach 1
TreeNode* mirror(TreeNode* root) {
    if (root == nullptr) {
        return nullptr;
    }

    mirror(root->left);
    mirror(root->right);

    TreeNode* temp = root->left;
    root->left = root->right;
    root->right = temp;

    return root;
}

// Approach 2
TreeNode* mirror(TreeNode* root) {
    if (root == nullptr) {
        return nullptr;
    }

    swap(root->left, root->right);

    mirror(root->left);
    mirror(root->right);

    return root;
}



// 2415. Reverse Odd Levels (Values) of Binary Tree
void traverse(TreeNode* root1, TreeNode* root2, int level) {
    if (root1 == nullptr || root2 == nullptr) {
        return;
    }

    if (level % 2 == 1) {
        swap(root1->val, root2->val);
    }

    traverse(root1->left, root2->right, level + 1);
    traverse(root1->right, root2->left, level + 1);
}

TreeNode* reverseOddLevels(TreeNode* root) {
    if (root == nullptr) {
        return nullptr;
    }

    traverse(root->left, root->right, 1);
    return root;
}




// 101. Symmetric Tree is BT which is a Mirror image of itself.
bool solve(TreeNode* root1, TreeNode* root2) {
    if (root1 == nullptr && root2 == nullptr) {
        return true;
    }
    if (root1 == nullptr || root2 == nullptr) {
        return false;
    }

    if (root1->val != root2->val) {
        return false;
    }

    bool x = solve(root1->left, root2->right);
    bool y = solve(root1->right, root2->left);
    return x && y;
}

bool isSymmetric(TreeNode* root) {
    if (root == nullptr) {
        return true;
    }

    return solve(root->left, root->right);
}



// 100. Same Tree
bool isSameTree(TreeNode* root1, TreeNode* root2) {
    if (root1 == nullptr && root2 == nullptr) {
        return true;
    }
    if (root1 == nullptr || root2 == nullptr || root1->val != root2->val) {
        return false;
    }

    bool left = isSameTree(root1->left, root2->left);
    bool right = isSameTree(root1->right, root2->right);

    return left && right;
}




// 654. Maximum Binary Tree
// 998. Maximum Binary Tree II