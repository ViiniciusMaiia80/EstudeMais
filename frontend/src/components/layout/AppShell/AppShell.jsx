import Topbar from "../Topbar/Topbar";
import Sidebar from "../Sidebar/Sidebar";

function AppShell({ children }) {
  return (
    <div className="min-h-screen bg-white flex">
      <Sidebar />
      <div className="flex-1 flex flex-col">
        <Topbar />
        <main className="flex-1 p-8">{children}</main>
      </div>
    </div>
  );
}

export default AppShell;
