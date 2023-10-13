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

// 653. Two Sum IV - Input is a BST
void inorder(TreeNode* root, vector<int>& temp) {
    if (root == nullptr) return;

    inorder(root->left, temp);
    temp.push_back(root->val);
    inorder(root->right, temp);
}

bool findTarget(TreeNode* root, int k) {
    vector<int> temp;
    inorder(root, temp);

    int low = 0;
    int high = temp.size() - 1;

    while(low < high) {
        int sum = temp[low] + temp[high];
        if(sum == k)
            return true;
        else if (sum > k) 
            high--;
        else
            low++;
    }

    return false;
}



// Floor and Ceil in BST 
// Brute Force
void inorder(TreeNode* root, vector<int>& temp) {
    if (root == nullptr) return;

    inorder(root->left, temp);
    temp.push_back(root->val);
    inorder(root->right, temp);
}

int floor(TreeNode* root, int x) {
    vector<int> temp;
    inorder(root, temp);
    int k = -1;
    for(int i = 0; i < temp.size(); i++) {
        if(temp[i] == x) {
            k = temp[i];
            break;
        } 
        else if(temp[i] < x) {
            k = temp[i];
        }
    }
    return k;
}

// Optimal Approach 
int floor(TreeNode* root, int x) {
    int res = -1;
    while(root != nullptr) {
        if(x == root->val) {
            res = root->val;
            return res;
        }
        if(root->val < x) {
            res = root->val;
            root = root->right;
        } else {
            root = root->left;
        }
    }
    return res;
}


// Ceil in BST 
int findCeil(Node* root, int x) {
    int res = -1;
    while(root != nullptr) {
        if(x == root->data) {
            res = root->data;
            return res;
        }
        if(root->data < x) {
            root = root->right;
        } else {
            res = root->data;
            root = root->left;  
        }
    }
    return res;
}



// Find the Closest Element in BST 
void solve(TreeNode* root, int k, int& mindiff) {
    if(root == nullptr) return;

    int diff = abs(k - root->data);
    if(diff < mindiff)
        mindiff = diff;

    solve(root->left, k, mindiff);
    solve(root->right, k, mindiff);
}

int minDiff(TreeNode* root, int k) {
    int mindiff = INT_MAX;
    solve(root, k, mindiff);
    return mindiff;
}