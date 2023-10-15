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


// 1305. All Elements in Two Binary Search Tree 
void inorder(TreeNode* root, vector<int>& ans) {
    if(root == nullptr) return;

    inorder(root->left, ans);
    ans.push_back(root->val);
    inorder(root->right, ans);
}

vector<int> getAllElements(TreeNode* root1, TreeNode* root2) {
    vector<int> temp1;
    vector<int> temp2;

    inorder(root1, temp1);
    inorder(root2, temp2);
    vector<int> res;
    int i = 0;
    int j = 0;
    while(i < temp1.size() || j < temp2.size()) {
        if(i < temp1.size() && (j == temp2.size() || temp1[i] < temp2[j])) {
            res.push_back(temp1[i]);
            i++;
        } else if(j < temp2.size()) {
            res.push_back(temp2[j]);
            j++;
        }
    }
    return res;
}




// Find Common Nodes in two BSTs
void inorder(TreeNode* root, vector<int>& ans) {
    if(root == nullptr) return;

    inorder(root->left, ans);
    ans.push_back(root->val);
    inorder(root->right, ans);
}

vector<int> commonNodes(TreeNode* root1, TreeNode* root2) {
    vector<int> temp1;
    vector<int> temp2;

    inorder(root1, temp1);
    inorder(root2, temp2);
    vector<int> res;
    int i = 0;
    int j = 0;
    while(i < temp1.size() && j < temp2.size()) {
        if(temp1[i] < temp2[j])
            i++;
        else if(temp1[i] > temp2[j])
            j++;
        else {
            res.push_back(temp1[i]);
            i++;
            j++;
        }
    }
}

