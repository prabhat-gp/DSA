# Inorder Predecessor and Successor

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

pair<int, int> predecessorSuccessor(TreeNode* root, key) {
    TreeNode* temp = root;
    int pred = -1;
    int succ = -1;

    while(temp->val != key) {
        if(temp->val > key) {
            succ = temp->val;
            temp = temp->left;
        }
        else {
            pred = temp->val;
            temp = temp->right;
        }
    }

    TreeNode* leftTree = temp->left;
    while(leftTree != NULL) {
        pred = leftTree->val;
        leftTree = leftTree->right;
    }

    TreeNode* rightTree = temp->left;
    while(rightTree != NULL) {
        succ = rightTree->val;
        rightTree = rightTree->right;
    }

    pair<int, int> ans = make_pair(pred, succ);
    return ans;
}