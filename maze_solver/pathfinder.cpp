#include <iostream>
#include <vector>
#include <windows.h>
using namespace std;

extern "C"{



    void clear_screen(char fill = ' ') {
        COORD tl = {0,0};
        CONSOLE_SCREEN_BUFFER_INFO s;
        HANDLE console = GetStdHandle(STD_OUTPUT_HANDLE);   
        GetConsoleScreenBufferInfo(console, &s);
        DWORD written, cells = s.dwSize.X * s.dwSize.Y;
        FillConsoleOutputCharacter(console, fill, cells, tl, &written);
        FillConsoleOutputAttribute(console, s.wAttributes, cells, tl, &written);
        SetConsoleCursorPosition(console, tl);
    }



    vector<vector<int>> pathfinder(vector<vector<int>>& mat, vector<int>& current, const vector<int>& end, vector<vector<int>>& cools) {

        cools.push_back(current);
        mat[current[0]][current[1]] = 1;

        if (current[0] == end[0] && current[1] == end[1]) {
            return cools;
        } else {
            vector<vector<int>> neighbours; // possible next steps
            if (mat[current[0] - 1][current[1]] != 1) {
                neighbours.push_back({current[0] - 1, current[1]});
            }
            if (mat[current[0] + 1][current[1]] != 1) {
                neighbours.push_back({current[0] + 1, current[1]});
            }
            if (mat[current[0]][current[1] - 1] != 1) {
                neighbours.push_back({current[0], current[1] - 1});
            }
            if (mat[current[0]][current[1] + 1] != 1) {
                neighbours.push_back({current[0], current[1] + 1});
            }

            if (neighbours.empty()) {
                return {};
            }

            vector<vector<vector<int>>> reslist;
            if(neighbours.size() == 1){
                auto res = pathfinder(mat, neighbours[0], end, cools);
                if(!res.empty()){
                    reslist.push_back(res);
                }
            }
            else{
                for (auto i : neighbours) {
                    auto newmat = mat;
                    auto newcools = cools;
                    auto res = pathfinder(newmat, i, end, newcools);
                    if (!res.empty()) {
                        reslist.push_back(res);
                    }
                }
            }


            if (reslist.empty()) {
                return {};
            }
            int id = 0;
            for(int i = 0; i < reslist.size(); i++){
                if(reslist[id].size() > reslist[i].size()){
                    id = i;
                }
            }
            return reslist[id];
        }
    }

    vector<vector<int>> buildMatrix(int * mat, int sizeX, int sizeY){
        vector<vector<int>> matrix;
        for(int i = 0; i < sizeX; i++){
            vector<int> row;
            for(int j = 0; j < sizeY; j++){
                row.push_back(mat[i*sizeX + j]);
            }
            matrix.push_back(row);
        }
        return matrix;
    }

    void directionPrinter(vector<vector<int>> route){
        if(route.empty()){
            cout<<"None"<<endl;
            return;
        }
        cout<<"S ";
        for(int i = 0; i < route.size(); i++){
            if (i != 0){
                if (route[i-1][1]+1 == route[i][1]){
                    cout<<"R ";
                }
                else if(route[i-1][1]-1 == route[i][1]){
                    cout<<"L ";
                }
                else if(route[i-1][0]+1 == route[i][0]){
                    cout<<"D ";
                }
                else if(route[i-1][0]-1 == route[i][0]){
                    cout<<"U ";
                }
            }
        }
        cout<<"G"<<endl;
    }

    void Test(){
        cout<<"Haha"<<endl;
    }

    void find_path(int * mat, int matsizeX, int matsizeY, int* _end, int* _start){
        vector<vector<int>> matrix = buildMatrix(mat, matsizeX, matsizeY);
        vector<int> start;
        vector<int> end;
        end.push_back(_end[0]);
        end.push_back(_end[1]);
        start.push_back(_start[0]);
        start.push_back(_start[1]);

        vector<vector<int>> coolinit;
        vector<vector<int>> result = pathfinder(matrix, start, end, coolinit);
        directionPrinter(result);

    }
}