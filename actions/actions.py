# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher

# class ActionUtterAVDMembuatActivityH5P(Action):
#     def name(self) -> Text:
#         return "A_V_D_Membuat_Activity_H5P"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         msg = {
#             "type": "video",
#             "payload": {
#                 "title": "Membuat Activity H5P",
#                 "src": "https://res.cloudinary.com/drood0vmn/video/upload/v1745630290/uploads/1745630223735-LeADS-Tutorial%20Dosen%20membuat%20Activity%20H5P%20%28Video%20Interactive%29.mp4.mp4"
#             }
#         }
#         dispatcher.utter_message(
#             text="Video ini akan menjelaskan kepada anda cara membuat activity dengan fitur HTML 5 Package yang berguna untuk menambahkan konten interaktif seperti presentasi, video, pertanyaan dan kuis",
#             attachment=msg
#         )
#         return []

# class ActionUtterAVDMembuatQuiz(Action):
#     def name(self) -> Text:
#         return "A_V_D_Membuat_Quiz"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         msg = {
#             "type": "video",
#             "payload": {
#                 "title": "Membuat Quiz",
#                 "src": "https://res.cloudinary.com/drood0vmn/video/upload/v1745630489/uploads/1745630436640-LeADS-Tutorial%20Dosen%20Membuat%20Quiz.mp4.mp4"
#             }
#         }
#         dispatcher.utter_message(
#             text="Video ini akan menjelaskan anda cara membuat kuis. Bentuk pertanyaan di dalam kuis bisa berbagai model. Mulai dari pilihan ganda, uraian, benar/salah dan sebagainya.",
#             attachment=msg
#         )
#         return []

# class ActionUtterAVDMengimporKuisDenganBlackboard(Action):
#     def name(self) -> Text:
#         return "A_V_D_Mengimpor_Kuis_Dengan_Blackboard"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         msg = {
#             "type": "video",
#             "payload": {
#                 "title": "Mengimpor Kuis dengan BlackBoard",
#                 "src": "https://res.cloudinary.com/drood0vmn/video/upload/v1745630810/uploads/1745630759826-Cara%20Mengimpor%20Kuis%20dengan%20BlackBoard.mp4.mp4"
#             }
#         }
#         dispatcher.utter_message(
#             text="Video ini akan menjelaskan anda bagaimana mengimport kuis yang dibuat dengan aplikasi BlackBoard ke dalam LeADS",
#             attachment=msg
#         )
#         return []

# class ActionUtterAVDMembuatActivity(Action):
#     def name(self) -> Text:
#         return "A_V_D_Membuat_Activity"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         msg = {
#             "type": "video",
#             "payload": {
#                 "title": "Membuat Activity",
#                 "src": "https://res.cloudinary.com/drood0vmn/video/upload/v1745631191/uploads/1745631143853-LeADS-Tutorial%20Dosen%20Membuat%20Activity%20%28File%2C%20Label%2C%20Page%2C%20Forum%2C%20dan%20Chat%29.mp4.mp4"
#             }
#         }
#         dispatcher.utter_message(
#             text="Video ini akan menjelaskan kepada anda bagaimana membuat Activity dengan jenis activity yang bervariasi. Dari video ini berbagai jenis activity yang dibuat yaitu Upload File (Materi, Bahan Ajar, dsb), Label (Menampilkan Video), Page (Menambahkan halaman website), Forum (Ruang Diskusi Interaktif) dan Chat (Ruang berdiskusi secara realtime)",
#             attachment=msg
#         )
#         return []

# class ActionUtterAVDMembuatVideoConference(Action):
#     def name(self) -> Text:
#         return "A_V_D_Membuat_Video_Conference"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         msg = {
#             "type": "video",
#             "payload": {
#                 "title": "Membuat Video Conference",
#                 "src": "https://res.cloudinary.com/drood0vmn/video/upload/v1745631368/uploads/1745631322025-LeADS-Tutorial%20Dosen%20Membuat%20Video%20Conference%20%28GMeet%29.mp4.mp4"
#             }
#         }
#         dispatcher.utter_message(
#             text="Video ini akan menjelaskan kepada anda bagaimana membuat Video Conference dalam LeADS",
#             attachment=msg
#         )
#         return []

# class ActionUtterAVDMengubahProfile(Action):
#     def name(self) -> Text:
#         return "A_V_D_Mengubah_Profile"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         msg = {
#             "type": "video",
#             "payload": {
#                 "title": "Mengubah Profile",
#                 "src": "https://res.cloudinary.com/drood0vmn/video/upload/v1745631455/uploads/1745631425971-Tutorial%20Mengubah%20Foto%20Profil%20dan%20Alamat%20Email.mp4.mp4"
#             }
#         }
#         dispatcher.utter_message(
#             text="Video ini akan menjelaskan kepada anda bagaimana mengubah data pribadi akun LeADS anda",
#             attachment=msg
#         )
#         return []

# class ActionUtterAVDMelakukanBackupRestoreCourse(Action):
#     def name(self) -> Text:
#         return "A_V_D_Melakukan_Backup_Restore_Course"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         msg = {
#             "type": "video",
#             "payload": {
#                 "title": "Backup dan Restore Course",
#                 "src": "https://res.cloudinary.com/drood0vmn/video/upload/v1745631637/uploads/1745631611820-LeADS-Tutorial%20Dosen%20Melakukan%20Backup%20dan%20Restore%20Course.mp4.mp4"
#             }
#         }
#         dispatcher.utter_message(
#             text="Video ini akan menjelaskan anda bagaimana memanfaatkan backup dan restore course. Berguna jika ingin menggunakan kembali course yang dibuat untuk periode berikutnya",
#             attachment=msg
#         )
#         return []

# class ActionUtterAVDMembuatPresensiMahasiswa(Action):
#     def name(self) -> Text:
#         return "A_V_D_Membuat_Presensi_Mahasiswa"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         msg = {
#             "type": "video",
#             "payload": {
#                 "title": "Membuat Presensi Mahasiswa",
#                 "src": "https://res.cloudinary.com/drood0vmn/video/upload/v1745631769/uploads/1745631743946-LeADS-Tutorial%20Dosen%20Membuat%20Presensi%20Mahasiswa%20menggunakan%20Attendance.mp4.mp4"
#             }
#         }
#         dispatcher.utter_message(
#             text="Video ini menjelaskan bagaimana cara membuat Presensi Mahasiswa menggunakan fitur Attendance dari LeADS",
#             attachment=msg
#         )
#         return []

# class ActionUtterAVDMembuatActivityAssignment(Action):
#     def name(self) -> Text:
#         return "A_V_D_Membuat_Activity_Assignment"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         msg = {
#             "type": "video",
#             "payload": {
#                 "title": "Membuat Activity Assignment",
#                 "src": "https://res.cloudinary.com/drood0vmn/video/upload/v1745631895/uploads/1745631865561-LeADS-Tutorial%20Dosen%20Membuat%20Activity%20Assignment.mp4.mp4"
#             }
#         }
#         dispatcher.utter_message(
#             text="Video ini akan menjelaskan bagaimana cara membuat assignment(penugasan) dalam LeADS",
#             attachment=msg
#         )
#         return []

# class ActionUtterAVMCaraMengumpulkanTugas(Action):
#     def name(self) -> Text:
#         return "A_V_M_Cara_Mengumpulkan_Tugas"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         msg = {
#             "type": "video",
#             "payload": {
#                 "title": "Cara Mengumpulkan Tugas",
#                 "src": "https://res.cloudinary.com/drood0vmn/video/upload/v1745632380/uploads/1745632347623-LeADS-Tutorial%20Mahasiswa%20Mengumpulkan%20Tugas.mp4.mp4"
#             }
#         }
#         dispatcher.utter_message(
#             text="Video ini akan menjelaskan anda bagaimana cara mengumpulkan tugas yang diberikan dosen anda",
#             attachment=msg
#         )
#         return []

# class ActionUtterAVMMenjawabSoalH5P(Action):
#     def name(self) -> Text:
#         return "A_V_M_Menjawab_Soal_H5P"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         msg = {
#             "type": "video",
#             "payload": {
#                 "title": "Menjawab Soal H5P",
#                 "src": "https://res.cloudinary.com/drood0vmn/video/upload/v1745632489/uploads/1745632466816-LeADS-Tutorial%20Mahasiswa%20Menjawab%20Soal%20H5P%20Video%20Interactive.mp4.mp4"
#             }
#         }
#         dispatcher.utter_message(
#             text="Video ini menjelaskan bagaimana anda mengerjakan tugas yang berbentuk H5P",
#             attachment=msg
#         )
#         return []

# class ActionUtterAVMMengisiKehadiran(Action):
#     def name(self) -> Text:
#         return "A_V_M_Mengisi_Kehadiran"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         msg = {
#             "type": "video",
#             "payload": {
#                 "title": "Mengisi Kehadiran",
#                 "src": "https://res.cloudinary.com/drood0vmn/video/upload/v1745632569/uploads/1745632554369-LeADS-Tutorial%20Mahasiswa%20mengisi%20Kehadiran%20di%20Perkuliahan.mp4.mp4"
#             }
#         }
#         dispatcher.utter_message(
#             text="Video ini menjelaskan bagaimana mengisi kehadiran perkuliahan di LeADS",
#             attachment=msg
#         )
#         return []

# class ActionUtterAVMMengikutiPerkuliahanViaVideoConference(Action):
#     def name(self) -> Text:
#         return "A_V_M_Mengikuti_Perkuliahan_Via_Video_Conference"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         msg = {
#             "type": "video",
#             "payload": {
#                 "title": "Mengikuti Perkuliahan Via Video Conference",
#                 "src": "https://res.cloudinary.com/drood0vmn/video/upload/v1745632684/uploads/1745632662863-LeADS-Tutorial%20Mahasiswa%20mengikuti%20Perkuliahan%20via%20Video%20Conference.mp4.mp4"
#             }
#         }
#         dispatcher.utter_message(
#             text="Video ini menjelaskan cara untuk mengikuti Video Conference dalam perkuliahan di LeADS",
#             attachment=msg
#         )
#         return []
