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

// Inorder of BST is sorted

// Min/Max Value of BST
TreeNode* minVal(TreeNode* root) {
    TreeNode* temp = root;

    while(temp->left != NULL) {
        temp = temp->left;
    }
    return temp;
}



TreeNode* maxVal(TreeNode* root) {
    TreeNode* temp = root;

    while(temp->right != NULL) {
        temp = temp->right;
    }
    return temp;
}



// Delete a Node in BST (Hard Question)
TreeNode* deleteFromBST(TreeNode* root, int k) {
    if(root == nullptr) {
        return root;
    }
    TreeNode* temp = root;

    if(temp->data == k) {
        if(temp->left == nullptr && temp->right == nullptr) {
            delete temp;
            return NULL;
        }

        if(temp-left != nullptr && temp->right == nullptr) {
            TreeNode* curr = temp;
            delete temp;
            return curr;
        }

        if(temp-left == nullptr && temp->right != nullptr) {
            TreeNode* curr = temp;
            delete temp;
            return curr;
        }

        if(temp->left != NULL && temp->right != NULL) {
            int mini = minVal(temp->right) -> val;
            temp->data = mini;
            temp->right = deleteFromBST(temp->right, mini);
            return temp;
        }
    } 
    else if(temp->val < k) {
        temp->right = deleteFromBST(temp->right, k);
        return temp;
    } 
    else {
        temp->left = deleteFromBST(temp->right, val);
        return temp;
    }

    return temp;
}

