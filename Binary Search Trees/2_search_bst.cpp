// 700. Search in a Binary Search Tree

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

// Recursive Approch
TreeNode* searchBST(TreeNode* root, int val) {
    if(root == NULL || root->val == val) return root;

    if(root->val < val) {
        return searchBST(root->right, val);
    } else {
        return searchBST(root->left, val);
    }
}



//  Iterative Approach
TreeNode* searchBST(TreeNode* root, int val) {
    TreeNode* temp = root;

    while (temp != nullptr) {
        if (temp->val == val) {
            return temp;
        }

        if(temp->val < val) {
            temp = temp->right;
        } else {
            temp = temp->left;
        }
    }
    return nullptr;    
}



// 701. Insert into a Binary Search Tree 
TreeNode* insertIntoBST(TreeNode* &root, int val) {
    if (root == NULL) {
        root = new TreeNode(val);
        return root;
    }

    if (val > root->val) {
        root->right = insertIntoBST(root->right, val);
    } else {
        root->left = insertIntoBST(root->left, val);
    }

    return root;
}
