// 236. Lowest Common Ancestor of a Binary Tree 

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


// Approach (works for both bt and bst) 
TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* r1, TreeNode* r2) {
    if(root == nullptr) return nullptr;

    if(root->val ==  r1 || root->val == r2) return root;

    TreeNode* leftAns = lowestCommonAncestor(root->left, r1, r2);
    TreeNode* rightAns = lowestCommonAncestor(root->right, r1, r2);

    if(leftAns != nullptr && rightAns != nullptr) 
        return root;
    else if(leftAns != nullptr && rightAns == nullptr) 
        return leftAns;
    else if(leftAns == nullptr && rightAns != nullptr)    
        return rightAns;
    else 
        return nullptr;
}



// 235. Lowest Common Ancestor of a Binary Search Tree 
// Efficient way of searching LCA

// Approach 1
TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* r1, TreeNode* r2) {
    if(root == nullptr) return nullptr;

    if(root->val < r1->val && root->val < r2->val) {
        return lowestCommonAncestor(root->right, r1, r2);
    }

    if(root->val > r1->val && root->val > r2->val) {
        return lowestCommonAncestor(root->left, r1, r2);
    }

    return root;
}



// Optimal Approach 
TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* r1, TreeNode* r2{
    if(root == nullptr) return nullptr;

    while (root != nullptr) {
        if (root->val < r1->val && root->val < r2->val)
            root = root->right;
        else if (root->val > r1->val && root->val > r2->val)
            root = root->left;
        else
            return root;
    }
    return nullptr;
}
